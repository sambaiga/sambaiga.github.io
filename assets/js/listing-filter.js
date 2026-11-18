// Topic chips, search and pagination for the Research page. The page marks its parts with data attributes: data-chip
// (a chip, "all" for no filter), data-search (the search box), data-item (a row with a data-topic), data-group (a year
// of rows with a data-count), data-empty (the message when nothing matches), and data-pager with data-size (rows per
// page) and data-pager-info. The page works without this script, which only hides what is not on the current page.
(function () {
  "use strict";
  var chips = document.querySelectorAll("[data-chip]");
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-item]"));
  var groups = document.querySelectorAll("[data-group]");
  var search = document.querySelector("[data-search]");
  var empty = document.querySelector("[data-empty]");
  var pager = document.querySelector("[data-pager]");
  var info = document.querySelector("[data-pager-info]");
  var size = pager ? Number(pager.getAttribute("data-size")) || 8 : Infinity;
  var state = { topic: "all", query: "", page: 1 };
  if (!chips.length) return;

  function matches(item) {
    return (
      (state.topic === "all" || item.getAttribute("data-topic") === state.topic) &&
      (state.query === "" || item.textContent.toLowerCase().indexOf(state.query) !== -1)
    );
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
      button('<i class="bi bi-chevron-left"></i><span class="ls-page-text">Previous</span>', page - 1, {
        aria: "Previous page",
        disabled: page === 1
      })
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
      button('<span class="ls-page-text">Next</span><i class="bi bi-chevron-right"></i>', page + 1, {
        aria: "Next page",
        disabled: page === pages
      })
    );
  }

  function apply() {
    var hits = items.filter(matches);
    var pages = Math.max(1, Math.ceil(hits.length / size));
    state.page = Math.min(state.page, pages);
    var first = (state.page - 1) * size;
    var shown = hits.slice(first, first + size);
    items.forEach(function (item) {
      item.hidden = shown.indexOf(item) === -1;
    });
    groups.forEach(function (group) {
      var count = 0;
      group.querySelectorAll("[data-item]").forEach(function (item) {
        if (hits.indexOf(item) !== -1) count += 1;
      });
      group.hidden = group.querySelectorAll("[data-item]:not([hidden])").length === 0;
      var label = group.querySelector("[data-count]");
      if (label) label.textContent = String(count);
    });
    if (empty) empty.hidden = hits.length !== 0;
    if (info) info.textContent = hits.length ? "Showing " + (first + 1) + "-" + (first + shown.length) + " of " + hits.length : "";
    drawPager(pages);
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      state.topic = chip.getAttribute("data-chip");
      state.page = 1;
      chips.forEach(function (other) {
        other.classList.toggle("active", other === chip);
      });
      apply();
    });
  });
  if (search)
    search.addEventListener("input", function () {
      state.query = search.value.trim().toLowerCase();
      state.page = 1;
      apply();
    });
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
  apply();
})();
