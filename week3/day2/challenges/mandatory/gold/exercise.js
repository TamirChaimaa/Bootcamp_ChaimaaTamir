const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];
const results = numbers.toString();
console.log(results);
console.log(numbers.join('+')); 
console.log(numbers.join(' '));  
console.log(numbers.join(''));   
const length = numbers.length;

// Outer loop for each pass
for (let i = 0; i < length; i++) {
  console.log(`Pass ${i + 1} begins:`, numbers);

  // Inner loop for comparing adjacent elements
  for (let j = 0; j < length - 1 - i; j++) {
    console.log(`  Comparing numbers[${j}] = ${numbers[j]} and numbers[${j + 1}] = ${numbers[j + 1]}`);

    // If the current element is less than the next, swap them (for descending order)
    if (numbers[j] < numbers[j + 1]) {
      console.log(`  Swapping ${numbers[j]} and ${numbers[j + 1]}`);

      let temp = numbers[j];                // Store current element in temp
      numbers[j] = numbers[j + 1];          // Move next element to current position
      numbers[j + 1] = temp;                // Put temp (original current element) in next position

      console.log(`  After swap:`, numbers);
    } else {
      console.log(`  No swap needed`);
    }
  }

  console.log(`Pass ${i + 1} ends:`, numbers);
}

// Final result after sorting
console.log('Final sorted array (descending):', numbers);