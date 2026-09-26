/* Home page effects: first-visit beige opening, SVG line-drawing entrance,
   laptop typewriter, projects popup, and a hand-drawn burst on click.
   Everything is skipped when the visitor prefers reduced motion. */
(function () {
  "use strict";

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- SVG line-drawing entrance ----------------------------------- */
  var startInkAnim = function () {
    var scene = document.querySelector(".desk-scene");
    if (!scene || reduceMotion) return;
    var groups = scene.querySelectorAll(".scene-link, .scene-desk, .scene-deco");
    groups.forEach(function (group, i) {
      group.style.setProperty("--i", i);
      var strokes = group.querySelectorAll("path[pathLength], circle[pathLength], ellipse[pathLength]");
      strokes.forEach(function (el, j) {
        el.style.setProperty("--i", i);
        el.style.setProperty("--j", j);
      });
    });
    document.body.classList.add("ink-anim");
  };

  /* ---- first-visit opening: bird walks a pencil line ---------------- */
  var overlay = document.getElementById("intro-overlay");
  var introSeen = false;
  try {
    introSeen = localStorage.getItem("xz-intro-played") === "1";
  } catch (e) { /* private mode etc. */ }

  if (overlay && !reduceMotion && !introSeen) {
    overlay.hidden = false;
    try { localStorage.setItem("xz-intro-played", "1"); } catch (e) {}

    var introDone = false;
    var endIntro = function () {
      if (introDone) return;
      introDone = true;
      overlay.classList.add("is-done");
      startInkAnim();
      window.setTimeout(function () { overlay.remove(); }, 500);
    };

    overlay.addEventListener("click", endIntro);
    window.setTimeout(endIntro, 2150);
  } else {
    if (overlay) overlay.remove();
    startInkAnim();
  }

  /* ---- typewriter on the laptop screen ------------------------------ */
  var screenText = document.querySelector(".laptop-screen__text");
  if (screenText) {
    var phrases = [
      "mapping cities",
      "uam simulation",
      "green space equity",
      "pedestrian svf",
      "llms x planning"
    ];

    if (reduceMotion) {
      screenText.textContent = phrases[0];
    } else {
      var phraseIndex = 0;
      var charIndex = 0;
      var deleting = false;

      var tick = function () {
        var phrase = phrases[phraseIndex];
        var delay;

        if (!deleting) {
          charIndex += 1;
          delay = 70;
          if (charIndex === phrase.length) {
            deleting = true;
            delay = 1700;
          }
        } else {
          charIndex -= 1;
          delay = 30;
          if (charIndex === 0) {
            deleting = false;
            phraseIndex = (phraseIndex + 1) % phrases.length;
            delay = 380;
          }
        }

        screenText.textContent = phrase.slice(0, charIndex);
        window.setTimeout(tick, delay);
      };

      window.setTimeout(tick, 1100);
    }
  }

  /* ---- selected-work popup next to the laptop ----------------------- */
  var wrap = document.querySelector(".desk-scene-wrap");
  var projectsLink = document.querySelector(".scene-link--projects");
  var popup = document.querySelector(".desk-popup");
  if (wrap && projectsLink && popup) {
    var hideTimer = null;
    var show = function () {
      window.clearTimeout(hideTimer);
      wrap.classList.add("show-popup");
    };
    var hide = function () {
      hideTimer = window.setTimeout(function () {
        wrap.classList.remove("show-popup");
      }, 180);
    };
    [projectsLink, popup].forEach(function (el) {
      el.addEventListener("mouseenter", show);
      el.addEventListener("mouseleave", hide);
      el.addEventListener("focusin", show);
      el.addEventListener("focusout", hide);
    });

    // The popup sits outside the SVG in the DOM, so route Tab through it by
    // hand: laptop -> popup links -> the next object on the desk (and back).
    var popupLinks = popup.querySelectorAll("a");
    var sceneLinks = Array.prototype.slice.call(document.querySelectorAll(".scene-link"));
    var afterProjects = sceneLinks[sceneLinks.indexOf(projectsLink) + 1];
    var first = popupLinks[0];
    var last = popupLinks[popupLinks.length - 1];

    projectsLink.addEventListener("keydown", function (event) {
      if (event.key === "Tab" && !event.shiftKey && first) {
        event.preventDefault();
        show();
        first.focus();
      }
    });
    popup.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        projectsLink.focus();
        wrap.classList.remove("show-popup");
      } else if (event.key === "Tab" && event.shiftKey && event.target === first) {
        event.preventDefault();
        projectsLink.focus();
      } else if (event.key === "Tab" && !event.shiftKey && event.target === last && afterProjects) {
        event.preventDefault();
        afterProjects.focus();
      }
    });
  }

  /* ---- hand-drawn burst on click ------------------------------------ */
  var BURST_SVG =
    '<svg viewBox="0 0 70 70" aria-hidden="true">' +
    '<path d="M35 4 L35 16 M57 13 L49 22 M66 35 L54 35 M57 57 L49 48 M35 66 L35 54 M13 57 L21 48 M4 35 L16 35 M13 13 L21 22"/>' +
    "</svg>";

  if (!reduceMotion && wrap) {
    document.querySelectorAll(".scene-link").forEach(function (link) {
      link.addEventListener("click", function (event) {
        var rect = wrap.getBoundingClientRect();
        var burst = document.createElement("span");
        burst.className = "click-burst";
        burst.style.left = event.clientX - rect.left + "px";
        burst.style.top = event.clientY - rect.top + "px";
        burst.innerHTML = BURST_SVG;
        wrap.appendChild(burst);
        window.setTimeout(function () { burst.remove(); }, 320);

        // Same-tab navigations wait a beat so the burst is visible.
        var href = link.getAttribute("href") || "";
        var sameTab = link.getAttribute("target") !== "_blank" && href.indexOf("mailto:") !== 0;
        if (sameTab && href) {
          event.preventDefault();
          window.setTimeout(function () { window.location = href; }, 210);
        }
      });
    });
  }
})();
