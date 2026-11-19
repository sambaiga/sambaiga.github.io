// The Research page: topic and type chips, search, sort, pagination, the Cite panel and the first-page preview.
// The page renders every paper without this script, which only shows the papers of the current page. It reads:
// data-chip (a topic chip, "all" for none), data-type-chip (journal, conference or "all"), data-search, data-sort,
// data-item (a paper, with data-topic, data-kind, data-date, data-title and data-text, the text that a search reads),
// data-count (the number of a year, when present), data-status, data-clear, data-empty, data-pager with data-size,
// data-pager-info, data-cite (a button, beside a template data-bibtex and a template data-reference), data-abstract (a
// button, beside a template data-abstract-text), data-preview
// (a button with the first page), and data-dialog with its data-dialog-title, -pdf, -image and -close.
(function () {
  "use strict";
  // The buttons that need this script are shown only once it runs (the stylesheet hides them until then)
  document.body.classList.add("pubs-js");
  var topicChips = document.querySelectorAll("[data-chip]");
  var typeChips = document.querySelectorAll("[data-type-chip]");
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-item]"));
  var search = document.querySelector("[data-search]");
  var sort = document.querySelector("[data-sort]");
  var empty = document.querySelector("[data-empty]");
  var status = document.querySelector("[data-status]");
  var clear = document.querySelector("[data-clear]");
  var pager = document.querySelector("[data-pager]");
  var info = document.querySelector("[data-pager-info]");
  var list = document.querySelector("[data-list]");
  var size = pager ? Number(pager.getAttribute("data-size")) || 8 : Infinity;
  var state = { topic: "all", type: "all", query: "", sort: "new", page: 1 };
  if (!items.length) return;

  function filtering() {
    return state.topic !== "all" || state.type !== "all" || state.query !== "";
  }

  function attr(item, name) {
    return item.getAttribute(name) || "";
  }

  function matches(item) {
    return (
      (state.topic === "all" || item.getAttribute("data-topic") === state.topic) &&
      (state.type === "all" || item.getAttribute("data-kind") === state.type) &&
      (state.query === "" || attr(item, "data-text").indexOf(state.query) !== -1)
    );
  }

  function order(a, b) {
    if (state.sort === "title") return attr(a, "data-title").localeCompare(attr(b, "data-title"));
    var byDate = attr(a, "data-date").localeCompare(attr(b, "data-date"));
    return state.sort === "old" ? byDate : -byDate;
  }

  function button(label, page, options) {
    var el = document.createElement("button");
    el.type = "button";
    el.className = "ls-page" + (options.className ? " " + options.className : "");
    el.innerHTML = label;
    el.setAttribute("aria-label", options.aria);
    if (options.current) el.setAttribute("aria-current", "page");
    if (options.disabled) el.disabled = true;
    else el.setAttribute("data-page", String(page));
    return el;
  }

  function drawPager(pages) {
    if (!pager) return;
    pager.textContent = "";
    pager.hidden = pages <= 1;
    if (pages <= 1) return;
    var page = state.page;
    pager.appendChild(
      button('<i class="bi bi-chevron-left"></i><span class="ls-page-text">Previous</span>', page - 1, { aria: "Previous page", disabled: page === 1 })
    );
    for (var number = 1; number <= pages; number += 1) {
      pager.appendChild(
        button(String(number), number, {
          className: "ls-page--number",
          current: number === page,
          aria: number === page ? "Page " + number + ", current page" : "Go to page " + number
        })
      );
    }
    var compact = document.createElement("span");
    compact.className = "ls-page-compact";
    compact.textContent = "Page " + page + " of " + pages;
    pager.appendChild(compact);
    pager.appendChild(
      button('<span class="ls-page-text">Next</span><i class="bi bi-chevron-right"></i>', page + 1, { aria: "Next page", disabled: page === pages })
    );
  }

  function closeCites() {
    document.querySelectorAll(".pubs-cite").forEach(function (panel) {
      panel.remove();
    });
  }

  function apply() {
    closeCites();
    var hits = items.filter(matches).sort(order);
    var pages = Math.max(1, Math.ceil(hits.length / size));
    state.page = Math.min(state.page, pages);
    var first = size === Infinity ? 0 : (state.page - 1) * size;
    var shown = size === Infinity ? hits : hits.slice(first, first + size);
    items.forEach(function (item) {
      item.hidden = shown.indexOf(item) === -1;
    });
    if (sort && list) {
      shown.forEach(function (item) {
        list.appendChild(item); // the sort order is the order in the page
      });
    }
    if (empty) empty.hidden = hits.length !== 0;
    if (clear) clear.hidden = !filtering();
    if (status) status.textContent = filtering() ? hits.length + " of " + items.length + " papers" : "";
    if (info) info.textContent = hits.length ? "Showing " + (first + 1) + "-" + (first + shown.length) + " of " + hits.length : "";
    drawPager(pages);
  }

  function setActive(chips, current) {
    chips.forEach(function (chip) {
      chip.classList.toggle("active", chip === current);
    });
  }

  function reset() {
    state = { topic: "all", type: "all", query: "", sort: state.sort, page: 1 };
    setActive(topicChips, document.querySelector('[data-chip="all"]'));
    setActive(typeChips, document.querySelector('[data-type-chip="all"]'));
    if (search) search.value = "";
    apply();
  }

  topicChips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      state.topic = chip.getAttribute("data-chip");
      state.page = 1;
      setActive(topicChips, chip);
      apply();
    });
  });
  typeChips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      state.type = chip.getAttribute("data-type-chip");
      state.page = 1;
      setActive(typeChips, chip);
      apply();
    });
  });
  if (search)
    search.addEventListener("input", function () {
      state.query = search.value.trim().toLowerCase();
      state.page = 1;
      apply();
    });
  if (sort)
    sort.addEventListener("change", function () {
      state.sort = sort.value;
      state.page = 1;
      apply();
    });
  if (clear) clear.addEventListener("click", reset);
  if (pager)
    pager.addEventListener("click", function (event) {
      var target = event.target.closest("[data-page]");
      if (!target) return;
      state.page = Number(target.getAttribute("data-page"));
      apply();
      // The pager is drawn again, so the focus goes back to the button of the page now shown.
      var current = pager.querySelector('[aria-current="page"]') || pager.querySelector("[data-page]");
      if (current) current.focus({ preventScroll: true });
      var top = document.querySelector(".ls-controls");
      if (top) top.scrollIntoView({ behavior: "smooth", block: "start" });
    });

  // ---- Cite: a floating panel with the BibTeX entry and a plain reference ----
  function templateText(root, name) {
    var template = root.querySelector("template[" + name + "]");
    return template ? template.content.textContent : "";
  }

  function openCite(trigger) {
    var root = trigger.closest("[data-item]");
    var existing = root.querySelector(".pubs-cite:not(.pubs-cite--abstract)");
    closeCites();
    if (existing) return;
    var panel = document.createElement("div");
    panel.className = "pubs-cite";
    panel.setAttribute("role", "group");
    panel.setAttribute("aria-label", "Cite this paper");
    var formats = [
      { name: "BibTeX", text: templateText(root, "data-bibtex"), code: true },
      { name: "Reference", text: templateText(root, "data-reference"), code: false }
    ];
    var tabs = document.createElement("div");
    tabs.className = "pubs-cite-tabs";
    var body = document.createElement("div");
    var copy = document.createElement("button");
    copy.type = "button";
    copy.className = "ls-button ls-button--small";
    var current = formats[0];

    function show(format) {
      current = format;
      body.textContent = "";
      var el = document.createElement(format.code ? "pre" : "p");
      el.textContent = format.text.trim();
      body.appendChild(el);
      tabs.querySelectorAll("button").forEach(function (tab) {
        tab.setAttribute("aria-pressed", String(tab.textContent === format.name));
      });
    }

    formats.forEach(function (format) {
      var tab = document.createElement("button");
      tab.type = "button";
      tab.textContent = format.name;
      tab.addEventListener("click", function () {
        show(format);
      });
      tabs.appendChild(tab);
    });
    copy.innerHTML = '<i class="bi bi-clipboard"></i><span>Copy</span>';
    copy.addEventListener("click", function () {
      var done = function () {
        copy.querySelector("span").textContent = "Copied";
        copy.querySelector("i").className = "bi bi-check2";
        setTimeout(function () {
          copy.querySelector("span").textContent = "Copy";
          copy.querySelector("i").className = "bi bi-clipboard";
        }, 1600);
      };
      if (navigator.clipboard) navigator.clipboard.writeText(current.text.trim()).then(done, done);
    });
    panel.appendChild(tabs);
    panel.appendChild(body);
    panel.appendChild(copy);
    show(formats[0]);
    root.appendChild(panel);
  }

  function openAbstract(trigger) {
    var root = trigger.closest("[data-item]");
    var existing = root.querySelector(".pubs-cite--abstract");
    closeCites();
    if (existing) return;
    var panel = document.createElement("div");
    panel.className = "pubs-cite pubs-cite--abstract";
    panel.setAttribute("role", "group");
    panel.setAttribute("aria-label", "Abstract");
    var text = document.createElement("p");
    text.textContent = templateText(root, "data-abstract-text").trim();
    panel.appendChild(text);
    root.appendChild(panel);
  }

  document.addEventListener("click", function (event) {
    var abstract = event.target.closest("[data-abstract]");
    if (abstract) return openAbstract(abstract);
    var trigger = event.target.closest("[data-cite]");
    if (trigger) return openCite(trigger);
    if (!event.target.closest(".pubs-cite")) closeCites();
  });
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") closeCites();
  });

  // ---- Preview: the whole first page in a dialog ----
  var dialog = document.querySelector("[data-dialog]");
  if (dialog && typeof dialog.showModal === "function") {
    document.addEventListener("click", function (event) {
      var open = event.target.closest("[data-preview]");
      if (!open) return;
      dialog.querySelector("[data-dialog-title]").textContent = open.getAttribute("data-preview-title");
      dialog.querySelector("[data-dialog-image]").src = open.getAttribute("data-preview");
      var pdf = dialog.querySelector("[data-dialog-pdf]");
      var url = open.getAttribute("data-preview-pdf");
      pdf.hidden = !url;
      if (url) pdf.href = url;
      dialog.showModal();
    });
    dialog.querySelector("[data-dialog-close]").addEventListener("click", function () {
      dialog.close();
    });
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) dialog.close();
    });
  } else {
    document.querySelectorAll("[data-preview]").forEach(function (button) {
      button.addEventListener("click", function () {
        window.open(button.getAttribute("data-preview"), "_blank", "noopener");
      });
    });
  }

  apply();
})();
