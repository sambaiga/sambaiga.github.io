// Topic chips and search for the listing pages. The page marks its parts with
// data attributes: data-chip (a chip, "all" for no filter), data-search (the
// search box), data-item (a row with a data-topic), data-group (a section of
// rows with a data-count) and data-empty (the message when nothing matches).
(function () {
  "use strict";
  var chips = document.querySelectorAll("[data-chip]");
  var items = document.querySelectorAll("[data-item]");
  var groups = document.querySelectorAll("[data-group]");
  var search = document.querySelector("[data-search]");
  var empty = document.querySelector("[data-empty]");
  var current = "all";
  if (!chips.length) return;

  function apply() {
    var query = search ? search.value.trim().toLowerCase() : "";
    var shown = 0;
    items.forEach(function (item) {
      var inTopic = current === "all" || item.getAttribute("data-topic") === current;
      var match = inTopic && (query === "" || item.textContent.toLowerCase().indexOf(query) !== -1);
      item.hidden = !match;
      if (match) shown += 1;
    });
    groups.forEach(function (group) {
      var visible = group.querySelectorAll("[data-item]:not([hidden])").length;
      group.hidden = visible === 0;
      var count = group.querySelector("[data-count]");
      if (count) count.textContent = String(visible);
    });
    if (empty) empty.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      current = chip.getAttribute("data-chip");
      chips.forEach(function (other) {
        other.classList.toggle("active", other === chip);
      });
      apply();
    });
  });
  if (search) search.addEventListener("input", apply);
})();
