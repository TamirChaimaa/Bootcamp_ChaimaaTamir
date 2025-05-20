const prompt = require("prompt-sync")();
do {
  number = parseInt(prompt("Enter a number:"));
} while (number < 10);

console.log("You entered a number 10 or greater.");