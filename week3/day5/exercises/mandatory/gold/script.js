
function playSound(key) {
  const audio = document.querySelector(`audio[data-key="${key.toUpperCase()}"]`);
  if (audio) {
    audio.currentTime = 0;
    audio.play();
  }
}

function animateButton(key) {
  const buttons = document.querySelectorAll(".btn");
  buttons.forEach((button) => {
    const btnKey = button.querySelector(".key").textContent;
    if (btnKey.toUpperCase() === key.toUpperCase()) {
      button.classList.add("active");
      setTimeout(() => {
        button.classList.remove("active");
      }, 150);
    }
  });
}

document.addEventListener("keydown", function (e) {
  playSound(e.key);
  animateButton(e.key);
});

const buttons = document.querySelectorAll(".btn");
buttons.forEach((button) => {
  button.addEventListener("click", function () {
    const key = this.querySelector(".key").textContent;
    playSound(key);
    animateButton(key);
  });
});

