// Function that compares a number to 10 and returns a Promise
function compareToTen(num) {
  return new Promise((resolve, reject) => {
    if (num <= 10) {
      // Resolve the promise if the number is less than or equal to 10
      resolve(`${num} is less than or equal to 10`);
    } else {
      // Reject the promise if the number is greater than 10
      reject(`${num} is greater than 10`);
    }
  });
}

// Test: should reject
compareToTen(15) // 15 is greater than 10
  .then(result => console.log(result))
  .catch(error => console.log(error));

// Test: should resolve
compareToTen(8) // 8 is less than or equal to 10
  .then(result => console.log(result))
  .catch(error => console.log(error));
