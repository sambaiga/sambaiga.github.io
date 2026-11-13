(function () {
  "use strict";
  var areas = document.querySelectorAll(".work-area");
  var chips = document.querySelectorAll(".work-areas a");
  var search = document.querySelector(".work-search");
  var empty = document.querySelector(".work-empty");
  var current = "all";

  function apply() {
    var query = search ? search.value.trim().toLowerCase() : "";
    var shown = 0;
    areas.forEach(function (area) {
      var inArea = current === "all" || area.id === "area-" + current;
      var visible = 0;
      area.querySelectorAll(".work-card").forEach(function (card) {
        var match = inArea && (query === "" || card.textContent.toLowerCase().indexOf(query) !== -1);
        card.hidden = !match;
        if (match) visible += 1;
      });
      area.hidden = visible === 0;
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
