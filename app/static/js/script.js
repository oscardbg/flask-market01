const modals = document.querySelectorAll(".modal");
const btnsInfo = document.querySelectorAll(".info");
//const btnsClose = modals.querySelectorAll("button");

btnsInfo.forEach((btn, index) => {
   btn.addEventListener("click", () => {
      modals[index].classList.add("active");
   });

   modals[index].querySelector("button").addEventListener("click", () => {
      modals[index].classList.remove("active");
   });
});
