// 1. input에 작성된 내용을 그대로 출력하기
const inputText = document.querySelector("#text-input");
inputText.addEventListener("input", function (event) {
  const copyText = document.querySelector("#text-paragraph");
  copyText.innerText = event.target.value;
});
