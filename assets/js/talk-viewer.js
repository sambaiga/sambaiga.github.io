// Slide viewer of the talk pages. It shows the pages of a PDF file one by one with pdf.js, which is kept in
// assets/vendor/pdfjs and loaded only on these pages. The page marks its parts with data attributes: data-viewer (the
// whole viewer, with data-pdf and data-lib), data-stage, data-canvas, data-prev, data-next, data-position,
// data-progress, data-strip, data-full, data-fallback, and data-copy with data-cite for the citation.
(function () {
  "use strict";
  var viewer = document.querySelector("[data-viewer]");
  var copy = document.querySelector("[data-copy]");

  function initCopy() {
    var cite = document.querySelector("[data-cite]");
    if (!copy || !cite) return;
    copy.addEventListener("click", function () {
      var label = copy.querySelector("span");
      var icon = copy.querySelector("i");
      var done = function () {
        label.textContent = "Copied";
        icon.className = "bi bi-check2";
        setTimeout(function () {
          label.textContent = "Copy citation";
          icon.className = "bi bi-clipboard";
        }, 1800);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(cite.textContent).then(done, done);
    });
  }
  initCopy();
  if (!viewer) return;

  var stage = viewer.querySelector("[data-stage]");
  var canvas = viewer.querySelector("[data-canvas]");
  var prev = viewer.querySelector("[data-prev]");
  var next = viewer.querySelector("[data-next]");
  var position = viewer.querySelector("[data-position]");
  var progress = viewer.querySelector("[data-progress]");
  var strip = viewer.querySelector("[data-strip]");
  var full = viewer.querySelector("[data-full]");
  var fallback = viewer.querySelector("[data-fallback]");
  var lib = viewer.getAttribute("data-lib");
  fallback.hidden = true;
  var doc = null;
  var current = 1;
  var task = null;
  var queued = null;

  function load(src) {
    return new Promise(function (resolve, reject) {
      var script = document.createElement("script");
      script.src = src;
      script.onload = resolve;
      script.onerror = reject;
      document.head.appendChild(script);
    });
  }

  // The slide is drawn as large as the stage allows, but never taller than 80 % of the window.
  function fit(page) {
    var base = page.getViewport({ scale: 1 });
    var style = getComputedStyle(stage);
    var width = stage.clientWidth - parseFloat(style.paddingLeft) - parseFloat(style.paddingRight);
    var height = Math.max(window.innerHeight * (document.fullscreenElement ? 0.9 : 0.8), 240);
    return Math.min(width / base.width, height / base.height);
  }

  function draw() {
    if (task) {
      queued = true;
      return;
    }
    task = doc.getPage(current).then(function (page) {
      var ratio = window.devicePixelRatio || 1;
      var scale = fit(page);
      var view = page.getViewport({ scale: scale * ratio });
      canvas.width = Math.floor(view.width);
      canvas.height = Math.floor(view.height);
      canvas.style.width = Math.floor(view.width / ratio) + "px";
      canvas.style.height = Math.floor(view.height / ratio) + "px";
      canvas.setAttribute("aria-label", "Slide " + current + " of " + doc.numPages);
      return page.render({ canvasContext: canvas.getContext("2d"), viewport: view }).promise;
    });
    task
      .catch(function () {})
      .then(function () {
        task = null;
        if (queued) {
          queued = null;
          draw();
        }
      });
  }

  function show(number) {
    current = Math.min(doc.numPages, Math.max(1, number));
    position.textContent = doc.numPages > 1 ? "Slide " + current + " of " + doc.numPages : "1 page";
    progress.style.width = (current / doc.numPages) * 100 + "%";
    prev.disabled = current === 1;
    next.disabled = current === doc.numPages;
    strip.querySelectorAll("button").forEach(function (button) {
      var on = Number(button.getAttribute("data-page")) === current;
      button.setAttribute("aria-current", on ? "true" : "false");
      if (on) strip.scrollTo({ left: button.offsetLeft - strip.clientWidth / 2 + button.clientWidth / 2, behavior: "smooth" });
    });
    if (history.replaceState) history.replaceState(null, "", current > 1 ? "#slide-" + current : location.pathname + location.search);
    draw();
  }

  function thumbnail(button, number) {
    doc.getPage(number).then(function (page) {
      var base = page.getViewport({ scale: 1 });
      var view = page.getViewport({ scale: 168 / base.width });
      var small = document.createElement("canvas");
      small.width = Math.floor(view.width);
      small.height = Math.floor(view.height);
      button.appendChild(small);
      page.render({ canvasContext: small.getContext("2d"), viewport: view });
    });
  }

  function buildStrip() {
    if (doc.numPages < 2) {
      strip.hidden = true;
      return;
    }
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          observer.unobserve(entry.target);
          thumbnail(entry.target, Number(entry.target.getAttribute("data-page")));
        });
      },
      { root: strip, rootMargin: "200px" }
    );
    for (var number = 1; number <= doc.numPages; number += 1) {
      var button = document.createElement("button");
      button.type = "button";
      button.setAttribute("data-page", String(number));
      button.setAttribute("aria-label", "Go to slide " + number);
      strip.appendChild(button);
      observer.observe(button);
    }
    strip.addEventListener("click", function (event) {
      var target = event.target.closest("button");
      if (target) show(Number(target.getAttribute("data-page")));
    });
  }

  function bind() {
    prev.addEventListener("click", function () {
      show(current - 1);
    });
    next.addEventListener("click", function () {
      show(current + 1);
    });
    document.addEventListener("keydown", function (event) {
      if (/INPUT|SELECT|TEXTAREA/.test(event.target.tagName) || event.altKey || event.ctrlKey || event.metaKey) return;
      if (event.key === "ArrowRight") show(current + 1);
      if (event.key === "ArrowLeft") show(current - 1);
    });
    var timer = null;
    window.addEventListener("resize", function () {
      clearTimeout(timer);
      timer = setTimeout(draw, 150);
    });
    if (full && viewer.requestFullscreen) {
      full.addEventListener("click", function () {
        if (document.fullscreenElement) document.exitFullscreen();
        else viewer.requestFullscreen();
      });
      document.addEventListener("fullscreenchange", draw);
    } else if (full) {
      full.hidden = true;
    }
    if (doc.numPages < 2) {
      prev.hidden = true;
      next.hidden = true;
      viewer.querySelector(".tp-keys").hidden = true;
    }
  }

  load(lib + "pdf.min.js")
    .then(function () {
      window.pdfjsLib.GlobalWorkerOptions.workerSrc = lib + "pdf.worker.min.js";
      return window.pdfjsLib.getDocument(viewer.getAttribute("data-pdf")).promise;
    })
    .then(function (loaded) {
      doc = loaded;
      viewer.classList.add("is-ready");
      bind();
      buildStrip();
      var start = /^#slide-(\d+)$/.exec(location.hash);
      show(start ? Number(start[1]) : 1);
    })
    .catch(function () {
      fallback.textContent = "The slides could not be shown here. ";
      var link = document.createElement("a");
      link.href = viewer.getAttribute("data-pdf");
      link.textContent = "Open the PDF file";
      fallback.appendChild(link);
      fallback.hidden = false;
    });
})();
