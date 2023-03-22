// const modal = document.querySelector(".modal_container");
// const modalContent = document.querySelector(".modal_content");
// function showModalAfterDelay() {
//   const modalShownKey = "modalShown";
//   const thirtySecondsInMs = 3000;
//   if (sessionStorage.getItem(modalShownKey)) {
//     return;
//   }
//   if (localStorage.getItem(modalShownKey)) {
//     localStorage.removeItem(modalShownKey);
//   } else {
//     setTimeout(() => {
//       modal.classList.add("modal_active");
//       modalContent.classList.add("modal_content_active");

//       localStorage.setItem(modalShownKey, true);
//     }, thirtySecondsInMs);
//   }
//   sessionStorage.setItem(modalShownKey, true);
// }
// function exitModal() {
  
//   modal.classList.remove("modal_active");
//   modalContent.classList.remove("modal_content_active");
// }


const modal = document.querySelector(".modal_container");
const modalContent = document.querySelector(".modal_content");
let ModalTime = 3000;
function ModalActive() {
  setTimeout(function () {
    modal.classList.add("modal_active");
    modalContent.classList.add("modal_content_active");
  }, ModalTime);
}
function exitModal() {
  modal.classList.remove("modal_active");
  modalContent.classList.remove("modal_content_active");
}