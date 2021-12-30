const infoModals = document.querySelectorAll(".infoModal");
const buyModals = document.querySelectorAll(".buyModal");
const sellModals = document.querySelectorAll(".sellModal");
const btnsInfo = document.querySelectorAll(".info");
const btnsBuy = document.querySelectorAll(".buy");
const btnsSell = document.querySelectorAll(".sell");

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

btnsSell.forEach((btn, index) => {
   btn.addEventListener("click", () => {
      sellModals[index].classList.add("active");
   });
   sellModals[index].querySelector(".close").addEventListener("click", () => {
      sellModals[index].classList.remove("active");
   });
});
