const prompt = require("prompt-sync")();
do {
  number = parseInt(prompt("Enter a number:"));
} while (number < 10);

console.log("You entered a number 10 or greater.");
//Why do...while? Because the condition (number < 10) is checked after the first execution — which allows the program to ask the user for input at least once, without requiring a condition beforehand.