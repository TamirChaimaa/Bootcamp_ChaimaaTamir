// Single loop
function drawPatternSingleLoop(lines) {
  let pattern = "";
  for (let i = 1; i <= lines; i++) {
    pattern += "* ".repeat(i) + "\n";
  }
  console.log(pattern);
}

// Call the function
drawPatternSingleLoop(6);


// Nested Loop
function drawPatternNestedLoops(lines) {
  let pattern = "";
  for (let i = 1; i <= lines; i++) {
    for (let j = 1; j <= i; j++) {
      pattern += "* ";
    }
    pattern += "\n";
  }
  console.log(pattern);
}

drawPatternNestedLoops(6);
