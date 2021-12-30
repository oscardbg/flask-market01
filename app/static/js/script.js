const infoModals = document.querySelectorAll(".infoModal");
const buyModals = document.querySelectorAll(".buyModal");
const btnsInfo = document.querySelectorAll(".info");
const btnsBuy = document.querySelectorAll(".buy");
//const btnsClose = modals.querySelectorAll("button");

btnsInfo.forEach((btn, index) => {
   btn.addEventListener("click", () => {
      infoModals[index].classList.add("active");
   });

   infoModals[index].querySelector(".close").addEventListener("click", () => {
      infoModals[index].classList.remove("active");
   });
});

btnsBuy.forEach((btn, index) => {
   btn.addEventListener("click", () => {
      buyModals[index].classList.add("active");
   });

   buyModals[index].querySelector(".close").addEventListener("click", () => {
      buyModals[index].classList.remove("active");
   });
});
