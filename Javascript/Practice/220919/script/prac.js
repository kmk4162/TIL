// 1. input에 작성된 내용을 그대로 출력하기
// const inputText = document.querySelector("#text-input");
// inputText.addEventListener("input", function (event) {
//   const copyText = document.querySelector("#text-paragraph");
//   copyText.innerText = event.target.value;
// });

// 2. 모달 직접 만들어보기
// 모달 버튼이 클릭되면
const modalToggle = function () {
  document.querySelector("#modal-content").classList.toggle("active");
};

const modalBtn = document.querySelector("#modal-btn");
modalBtn.addEventListener("click", modalToggle);

// 모달 취소 버튼이 클릭되면
const modalCancelBtn = document.querySelector("#modal-cancel-btn");
modalCancelBtn.addEventListener("click", modalToggle);

// 모달 오버레이를 클릭하면
const modalOverlay = document.querySelector("#modal-content");
modalOverlay.addEventListener("click", modalToggle);
