const prevBtn = document.querySelector("#prevBtn");

prevBtn.addEventListener("click", function () {
  const currentElement = document.querySelector(".active");
  const items = document.querySelectorAll(".carousel-item");
  const idx = [...items].indexOf(currentElement);
  console.log(currentElement, items, idx);
  currentElement.classList.toggle("active");
  items[(items.length + idx - 1) % items.length].classList.toggle("active");
});

const nextBtn = document.querySelector("#nextBtn");

nextBtn.addEventListener("click", function () {
  const currentElement = document.querySelector(".active");
  const items = document.querySelectorAll(".carousel-item");
  const idx = [...items].indexOf(currentElement);
  console.log(currentElement, items, idx);
  currentElement.classList.toggle("active");
  items[(idx + 1) % items.length].classList.toggle("active");
});

setInterval(function () {
  const nextBtn = document.querySelector("#nextBtn");
  nextBtn.click();
}, 10000);

document.addEventListener("load", function () {});
