// The chips of the Blog call the category filter of Quarto (window.quartoListingCategory). This script only marks the chip
// of the category in the address (#category=...), on loading and whenever the category changes.
(function () {
  "use strict";
  var chips = document.querySelectorAll(".ls-chips [data-category]");
  if (!chips.length) return;

  function mark() {
    var match = /category=([^&]*)/.exec(window.location.hash);
    var current = match ? decodeURIComponent(match[1]) : "";
    chips.forEach(function (chip) {
      chip.classList.toggle("active", chip.getAttribute("data-category") === current);
    });
  }

  window.addEventListener("hashchange", mark);
  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      window.setTimeout(mark, 0);
    });
  });
  mark();
})();
