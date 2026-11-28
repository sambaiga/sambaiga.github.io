// Books page: on a phone the description of a card is cut to three lines; a button opens and closes the whole text.
// The button is shown only for a description that is actually cut, so it never appears on a wide screen.
(function () {
  const cards = document.querySelectorAll(".tl-book");

  function cut(description) {
    return description.scrollHeight > description.clientHeight + 1;
  }

  function refresh() {
    cards.forEach((card) => {
      const description = card.querySelector(".tl-description");
      const button = card.querySelector(".tl-more");
      if (!description || !button) return;
      if (card.classList.contains("is-open")) return;
      button.hidden = !cut(description);
    });
  }

  cards.forEach((card) => {
    const description = card.querySelector(".tl-description");
    const button = card.querySelector(".tl-more");
    if (!description || !button) return;
    const toggle = () => {
      const open = card.classList.toggle("is-open");
      button.setAttribute("aria-expanded", String(open));
      button.querySelector("span").textContent = open ? "Show less" : "Read more";
      button.hidden = false;
      if (!open) refresh();
    };
    button.addEventListener("click", toggle);
    description.addEventListener("click", () => {
      if (!button.hidden) toggle();
    });
  });

  refresh();
  window.addEventListener("resize", refresh);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refresh);
})();
