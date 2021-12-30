const modal = document.querySelector(".modal");
const btn = document.querySelector(".info");
const btnClose = modal.querySelector("button");

btn.addEventListener("click", () => {
   modal.classList.add("active");
});
btnClose.addEventListener("click", () => {
   modal.classList.remove("active");
});
