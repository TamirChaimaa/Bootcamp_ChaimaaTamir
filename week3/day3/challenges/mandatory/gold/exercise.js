// Prompt the user for input
const prompt = require('prompt-sync')();
let input = prompt("Enter several words separated by commas:");
let words = input.split(',').map(word => word.trim());

let maxLength = Math.max(...words.map(word => word.length));

let border = '*'.repeat(maxLength + 4);

console.log(border);
words.forEach(word => {
    console.log(`* ${word.padEnd(maxLength)} *`);
});
console.log(border);
