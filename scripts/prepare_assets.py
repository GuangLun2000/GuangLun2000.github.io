"""Responsive images for every <img> in the site's pages. Run after adding or changing images.

For each local JPEG/PNG referenced by an <img> tag it:
  * adds width/height (from the file) and decoding="async" so the layout doesn't shift;
  * writes WebP copies at 320/480/640/960/1280/1600 px (never upscaled) to assets/responsive/,
    named <stem>-<content hash>-<width>.webp, and wraps the tag in a <picture> whose
    <source> lists them; the original file stays as the <img> fallback;
  * marks the one above-the-fold image per page (hero portrait, first Projects /
    Coursework card) fetchpriority="high" and never lazy; every other image gets
    loading="lazy";
  * keeps the home page's portrait <link rel="preload"> in _includes/head.html in step
    with the portrait's WebP sources.
Re-running is idempotent. --check exits 1 if any page or WebP would change.

Requires Pillow (pip install Pillow).
"""
from pathlib import Path
import hashlib
import io
import re
import sys
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'responsive'
CHECK = '--check' in sys.argv
WIDTHS = (320, 480, 640, 960, 1280, 1600)
changes = []

# rendered width of each image slot, matched to main.css
SIZES = {
    'portrait': '(max-width: 900px) 200px, 300px',
    'card': '(max-width: 767px) calc(100vw - 4.5rem), 450px',  # gutters + the card's image padding
    'feature': '(max-width: 900px) calc(100vw - 2.5rem), 360px',
    'article': '(max-width: 800px) calc(100vw - 2.5rem), 760px',
}


def save(path, data):
    if isinstance(data, str):
        data = data.encode('utf-8')
    if path.exists() and path.read_bytes().replace(b'\r\n', b'\n') == data.replace(b'\r\n', b'\n'):
        return
    changes.append(str(path.relative_to(ROOT)))
    if not CHECK:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def set_attr(tag, name, value):
    """Set (or with value=None, remove) an attribute on a single <img ...> tag."""
    tag = re.sub(rf'\s{name}="[^"]*"', '', tag)
    if value is None:
        return tag
    return re.sub(r'\s*/?>$', f' {name}="{value}">', tag)


def slot(page, src, tag):
    if 'xuanyu_web' in src:
        return 'portrait'
    if 'work-card__media' in tag:
        return 'card'
    if page == 'project-urban-built-env.md':
        return 'feature'
    return 'article'


def process(page, tag, first_card):
    src = re.search(r'src="([^"]+)"', tag)
    if not src or not src[1].startswith('/') or '{{' in src[1]:
        return tag
    path = ROOT / src[1].lstrip('/')
    if not path.is_file() or path.suffix.lower() not in ('.jpg', '.jpeg', '.png'):
        return tag

    kind = slot(page, src[1], tag)
    above_fold = kind == 'portrait' or (kind == 'card' and first_card)
    tag = set_attr(tag, 'loading', None if above_fold else 'lazy')
    tag = set_attr(tag, 'fetchpriority', 'high' if above_fold else None)
    tag = set_attr(tag, 'decoding', 'async')

    with Image.open(path) as original:
        image = ImageOps.exif_transpose(original)
        if image.mode in ('RGBA', 'LA', 'P'):
            # transparent PNGs (diagrams) sit on white; a plain RGB convert turns them black
            rgba = image.convert('RGBA')
            image = Image.new('RGB', rgba.size, (255, 255, 255))
            image.paste(rgba, mask=rgba.getchannel('A'))
        else:
            image = image.convert('RGB')
        width, height = image.size
        # the portrait's markup keeps its display ratio; everything else gets file dimensions
        if kind != 'portrait' or ' width=' not in tag:
            tag = set_attr(set_attr(tag, 'width', str(width)), 'height', str(height))
        if width < 400:
            return tag
        digest = hashlib.sha256(path.read_bytes()).hexdigest()[:12]
        # diagrams and maps (PNG sources) and text-heavy posters keep more detail
        quality = 90 if path.suffix.lower() == '.png' or 'poster' in path.stem else 80
        sources = []
        for size in sorted({min(width, n) for n in WIDTHS}):
            target = OUT / f'{path.stem}-{digest}-{size}.webp'
            if not target.exists():
                resized = image if size == width else image.resize(
                    (size, round(height * size / width)), Image.Resampling.LANCZOS)
                buf = io.BytesIO()
                resized.save(buf, 'WEBP', quality=quality, method=6)
                save(target, buf.getvalue())
            sources.append(f'/{target.relative_to(ROOT).as_posix()} {size}w')
    return ('<picture><source type="image/webp" srcset="' + ', '.join(sources)
            + f'" sizes="{SIZES[kind]}">' + tag + '</picture>')


pages = sorted(list(ROOT.glob('*.md')) + [ROOT / 'projects' / 'index.md'])
for path in pages:
    page = path.relative_to(ROOT).as_posix()
    text = path.read_text(encoding='utf-8-sig')
    # unwrap previous runs so the result only depends on the <img> tags
    text = re.sub(r'<picture><source type="image/webp"[^>]*>(<img\b[^>]*>)</picture>', r'\1', text)
    seen_card = False

    def repl(match):
        global seen_card
        tag = match.group()
        first = 'work-card__media' in tag and not seen_card
        if 'work-card__media' in tag:
            seen_card = True
        return process(page, tag, first)

    save(path, re.sub(r'<img\b[^>]*>', repl, text))

# keep the home page's portrait preload in step with its <picture> sources
head = ROOT / '_includes' / 'head.html'
portrait = re.search(r'<source type="image/webp" srcset="([^"]*xuanyu_web[^"]*)" sizes="([^"]*)">',
                     (ROOT / 'index.md').read_text(encoding='utf-8-sig'))
if portrait:
    tag = (f'<link rel="preload" as="image" type="image/webp" imagesrcset="{portrait[1]}" '
           f'imagesizes="{portrait[2]}" fetchpriority="high">')
    text = head.read_text(encoding='utf-8-sig')
    save(head, re.sub(r'(<!-- portrait-preload: [^>]*-->\s*)<link rel="preload" as="image"[^>]*>',
                      lambda m: m[1] + tag, text))

# drop WebP files no page references any more
if OUT.exists():
    used = set()
    for path in pages:
        used.update(re.findall(r'/assets/responsive/([^ "]+\.webp)', path.read_text(encoding='utf-8-sig')))
    for f in OUT.glob('*.webp'):
        if f.name not in used:
            changes.append(f'(unused) {f.relative_to(ROOT)}')
            if not CHECK:
                f.unlink()

print(('Outdated: ' if CHECK else 'Updated: ') + str(len(changes)) + ' files')
if changes:
    print('\n'.join(changes))
if CHECK and changes:
    sys.exit(1)
