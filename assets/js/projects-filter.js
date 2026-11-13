(function () {
  "use strict";
  var years = document.querySelectorAll(".tl-year");
  var chips = document.querySelectorAll(".tl-areas a");
  var search = document.querySelector(".tl-search");
  var empty = document.querySelector(".tl-empty");
  var current = "all";

  function apply() {
    var query = search ? search.value.trim().toLowerCase() : "";
    var shown = 0;
    years.forEach(function (year) {
      var visible = 0;
      year.querySelectorAll(".tl-item").forEach(function (item) {
        var inArea = current === "all" || item.getAttribute("data-area") === current;
        var match = inArea && (query === "" || item.textContent.toLowerCase().indexOf(query) !== -1);
        item.hidden = !match;
        if (match) visible += 1;
      });
      year.hidden = visible === 0;
      shown += visible;
    });
    if (empty) empty.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      current = chip.getAttribute("data-area");
      chips.forEach(function (other) {
        other.classList.toggle("active", other === chip);
      });
      apply();
    });
  });
  if (search) search.addEventListener("input", apply);
})();
