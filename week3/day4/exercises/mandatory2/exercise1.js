//In your Javascript file, using setTimeout, call a function after 2 seconds.
// 

function notifyAfterDelay() {
  setTimeout(() => {
    console.log("Hello World");
  }, 2000);
}

notifyAfterDelay();
setTimeout(() => {
  const container = document.getElementById("container");
  const paragraph = document.createElement("p");
  paragraph.textContent = "Hello World";
  container.appendChild(paragraph);
}, 2000);

