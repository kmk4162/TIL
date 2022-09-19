const myBtn = document.querySelector("#myBtn");
const alertMessage = function () {
  alert("히히!");
};
// 1
myBtn.addEventListener("click", alertMessage);

// 2
const myTextInput = document.querySelector("#my-text-input");

myTextInput.addEventListener("input", function (event) {
  // console.log(event);
  const myPtag = document.querySelector("#my-paragraph");
  myPtag.innerText = event.target.value;
});

// 3
const colorInput = document.querySelector("#change-color-input");

const changeColor = function (event) {
  const h2Tag = document.querySelector("h2");
  h2Tag.style.color = event.target.value;
};
colorInput.addEventListener("input", changeColor);

// 4
const checkBox = document.queryselector("#my-checkbox");
// console.log(checkBox);
checkBox.addEventListener("click", function (event) {
  event.preventDefault();
  console.log(event);
});
