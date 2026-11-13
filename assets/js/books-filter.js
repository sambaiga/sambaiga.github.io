(function () {
  "use strict";
  var books = document.querySelectorAll(".bk");
  var chips = document.querySelectorAll(".bk-genres a");
  var search = document.querySelector(".bk-search");
  var empty = document.querySelector(".bk-empty");
  var current = "all";
  if (!chips.length) return;

  function apply() {
    var query = search ? search.value.trim().toLowerCase() : "";
    var shown = 0;
    books.forEach(function (book) {
      var inGenre = current === "all" || book.getAttribute("data-genre") === current;
      var match = inGenre && (query === "" || book.textContent.toLowerCase().indexOf(query) !== -1);
      book.hidden = !match;
      if (match) shown += 1;
    });
    if (empty) empty.hidden = shown !== 0;
  }

  chips.forEach(function (chip) {
    chip.addEventListener("click", function (event) {
      event.preventDefault();
      current = chip.getAttribute("data-genre");
      chips.forEach(function (other) {
        other.classList.toggle("active", other === chip);
      });
      apply();
    });
  });
  if (search) search.addEventListener("input", apply);
})();
