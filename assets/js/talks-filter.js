// Type chips, topic select, search and pagination for the Talks page. The template renders every talk, so the page
// works without this script. The page marks its parts with data attributes: data-chip (a type chip, "all" for no
// filter), data-topic-select (the topic select), data-search, data-item (a talk card with data-type and data-topic), data-group (a year with a data-count),
// data-status, data-clear, data-empty, data-pager and data-pager-info.
(function () {
  "use strict";
  var PAGE = 12;
  var chips = document.querySelectorAll("[data-chip]");
  var items = Array.prototype.slice.call(document.querySelectorAll("[data-item]"));
  var groups = document.querySelectorAll("[data-group]");
  var select = document.querySelector("[data-topic-select]");
  var search = document.querySelector("[data-search]");
  var empty = document.querySelector("[data-empty]");
  var status = document.querySelector("[data-status]");
  var clear = document.querySelector("[data-clear]");
  var pager = document.querySelector("[data-pager]");
  var info = document.querySelector("[data-pager-info]");
  var list = document.querySelector("[data-list]");
  var state = { type: "all", topic: "all", query: "", page: 1 };
  if (!items.length) return;

  function matches(item) {
    var query = state.query;
    return (
      (state.type === "all" || item.getAttribute("data-type") === state.type) &&
      (state.topic === "all" || item.getAttribute("data-topic") === state.topic) &&
      (query === "" || item.textContent.toLowerCase().indexOf(query) !== -1)
    );
  }

  function button(label, page, extra) {
    var el = document.createElement("button");
    el.type = "button";
    el.className = "tk-page" + (extra && extra.className ? " " + extra.className : "");
    el.innerHTML = label;
    if (extra && extra.aria) el.setAttribute("aria-label", extra.aria);
    if (extra && extra.current) el.setAttribute("aria-current", "page");
    if (extra && extra.disabled) el.disabled = true;
    else el.setAttribute("data-page", String(page));
    return el;
  }

  function drawPager(pages) {
    pager.textContent = "";
    pager.hidden = pages <= 1;
    if (pages <= 1) return;
    var page = state.page;
    pager.appendChild(
      button('<i class="bi bi-chevron-left"></i><span class="tk-page-text">Previous</span>', page - 1, { aria: "Previous page", disabled: page === 1 })
    );
    for (var number = 1; number <= pages; number += 1) {
      pager.appendChild(
        button(String(number), number, {
          className: "tk-page--number",
          current: number === page,
          aria: number === page ? "Page " + number + ", current page" : "Go to page " + number
        })
      );
    }
    var compact = document.createElement("span");
    compact.className = "tk-page-compact";
    compact.textContent = "Page " + page + " of " + pages;
    pager.appendChild(compact);
    pager.appendChild(
      button('<span class="tk-page-text">Next</span><i class="bi bi-chevron-right"></i>', page + 1, { aria: "Next page", disabled: page === pages })
    );
  }

  function apply() {
    var hits = items.filter(matches);
    var pages = Math.max(1, Math.ceil(hits.length / PAGE));
    state.page = Math.min(state.page, pages);
    var first = (state.page - 1) * PAGE;
    var shown = hits.slice(first, first + PAGE);
    items.forEach(function (item) {
      item.hidden = shown.indexOf(item) === -1;
    });
    groups.forEach(function (group) {
      var total = group.querySelectorAll("[data-item]");
      var count = 0;
      total.forEach(function (item) {
        if (hits.indexOf(item) !== -1) count += 1;
      });
      group.hidden = group.querySelectorAll("[data-item]:not([hidden])").length === 0;
      var label = group.querySelector("[data-count]");
      if (label) label.textContent = String(count);
    });
    var filtered = state.type !== "all" || state.topic !== "all" || state.query !== "";
    if (empty) empty.hidden = hits.length !== 0;
    if (clear) clear.hidden = !filtered;
    if (status) status.textContent = filtered ? hits.length + " of " + items.length + " talks" : "";
    if (info) info.textContent = hits.length ? "Showing " + (first + 1) + "-" + (first + shown.length) + " of " + hits.length : "";
    drawPager(pages);
  }

  function reset() {
    state = { type: "all", topic: "all", query: "", page: 1 };
    chips.forEach(function (chip) {
      chip.classList.toggle("active", chip.getAttribute("data-chip") === "all");
    });
    if (select) select.value = "all";
    if (search) search.value = "";
    apply();
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      state.type = chip.getAttribute("data-chip");
      state.page = 1;
      chips.forEach(function (other) {
        other.classList.toggle("active", other === chip);
      });
      apply();
    });
  });
  if (select)
    select.addEventListener("change", function () {
      state.topic = select.value;
      state.page = 1;
      apply();
    });
  if (search)
    search.addEventListener("input", function () {
      state.query = search.value.trim().toLowerCase();
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
      if (list) list.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  apply();
})();
