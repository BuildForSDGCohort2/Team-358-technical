// simple JS I re-purposed from some place on Stackoverflow
// not essential for the CSS POC

var interval = setInterval(timerFunc, 10),
    mins = 00,
    seconds = 00,
    tens = 00,
    tensEl = document.getElementById("timerTens"),
    secondsEl = document.getElementById("timerSeconds"),
    minsEl = document.getElementById("timerMins");

function timerFunc() {
    console.log("hi");
    tens++;
    if (tens < 9) {
        tensEl.innerHTML = "0" + tens;
    }
    if (tens > 9) {
        tensEl.innerHTML = tens;
    }
    if (tens > 99) {
        seconds++;
        secondsEl.innerHTML = "0" + seconds;
        tens = 0;
        tensEl.innerHTML = "0" + 0;
    }
    if (seconds < 9) {
        secondsEl.innerHTML = "0" + seconds;
    }
    if (seconds > 9) {
        secondsEl.innerHTML = seconds;
    }
    if (seconds > 59) {
        secondsEl.innerHTML = 00;
        seconds = 00;
        mins++;
        minsEl.innerHTML = mins;
    }
    if (mins < 9) {
        minsEl.innerHTML = "0" + mins;
    }
}


//
const container = document.getElementById('container');
const text = document.getElementById('text');

const totalTime = 7500;
const breatheTime = (totalTime / 5) * 2;
const holdTime = totalTime / 5;

breathAnimation();

function breathAnimation() {
  text.innerText = 'Speak Now!';
  container.className = 'container grow';

  setTimeout(() => {
    text.innerText = 'Hold On';

    setTimeout(() => {
      text.innerText = 'Speak Again!';
      container.className = 'container shrink';
    }, holdTime);
  }, breatheTime);
}

setInterval(breathAnimation, totalTime);
