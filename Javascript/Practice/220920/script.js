const lottoBtn = document.querySelector("#lotto-btn");
lottoBtn.addEventListener("click", function () {
  const makeBall = document.createElement("div");
  makeBall.classList.add("ball-container");
  let numbers = _.sampleSize(_.range(1, 46), 6);
  numbers.sort(function (a, b) {
    return a - b;
  });
  console.log(numbers);
  for (let i = 0; i < 6; i++) {
    let ball = document.createElement("div");
    ball.classList.add("ball");
    ball.innerText = numbers[i];
    if (ball.innerText <= 10) {
      ball.style.backgroundColor = "rgb(255 213 105)";
    } else if (ball.innerText <= 20) {
      ball.style.backgroundColor = "rgb(62, 113, 172)";
    } else if (ball.innerText <= 30) {
      ball.style.backgroundColor = "rgb(255, 35, 2)";
    } else if (ball.innerText <= 40) {
      ball.style.backgroundColor = "rgb(65, 71, 84)";
    } else {
      ball.style.backgroundColor = "rgb(80, 178, 103)";
    }
    makeBall.appendChild(ball);
  }
  const result = document.querySelector("#result");
  result.appendChild(makeBall);
  // 1번부터 10번까지는 노란색입니다.
  // 11번 부터 20번까지는 파란색입니다.
  // 21번부터 30번까지는 빨간색입니다.
  // 31번부터 40번까지는 검은색입니다.
  // 41번부터 45번까지는 초록색입니다.
});
