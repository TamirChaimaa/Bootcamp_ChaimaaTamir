function move() {
  const elem = document.getElementById("animate");
  const container = document.getElementById("container");
  let pos = 0;

  const interval = setInterval(() => {
    if (pos >= container.clientWidth - elem.offsetWidth) {
      clearInterval(interval);
    } else {
      pos++;
      elem.style.left = pos + "px";
    }
  }, 1);
}
