#!/usr/bin/env sh
# Rebuild the self-hosted web fonts: instance the variable fonts to the axis
# ranges the site uses and subset them to Latin. Needs `pip install fonttools brotli`
# and the Fontsource packages (npm i @fontsource-variable/source-serif-4
# @fontsource-variable/instrument-sans) in $FONTSOURCE (default ./node_modules).
set -e
SRC="${FONTSOURCE:-node_modules}/@fontsource-variable"
OUT="$(dirname "$0")/../assets/fonts"
TMP="$(mktemp -d)"
U="U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+2010-2027,U+2030-203A,U+2190-2199,U+20AC"

build() { # <source woff2> <instancer axes> <features> <output name>
  python -m fontTools.varLib.instancer "$1" $2 -o "$TMP/x.woff2" --quiet
  python -m fontTools.subset "$TMP/x.woff2" --unicodes="$U" --layout-features="$3" \
    --flavor=woff2 --output-file="$OUT/$4"
}

build "$SRC/source-serif-4/files/source-serif-4-latin-opsz-normal.woff2" "opsz=20:60 wght=400:600" \
  kern,liga,calt,onum,lnum,pnum,tnum,case source-serif-4-display-latin.woff2
build "$SRC/source-serif-4/files/source-serif-4-latin-wght-italic.woff2" "wght=400:600" \
  kern,liga,calt source-serif-4-italic-latin.woff2
build "$SRC/instrument-sans/files/instrument-sans-latin-wght-normal.woff2" "wght=400:600" \
  kern,liga,calt,tnum instrument-sans-latin.woff2
build "$SRC/instrument-sans/files/instrument-sans-latin-wght-italic.woff2" "wght=400:600" \
  kern,liga,calt instrument-sans-italic-latin.woff2
rm -rf "$TMP"
