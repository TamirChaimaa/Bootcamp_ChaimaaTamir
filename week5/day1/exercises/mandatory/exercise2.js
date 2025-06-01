// Create a promise that resolves after 4 seconds
const promiseSuccess = new Promise((resolve, reject) => {
  setTimeout(() => {
    // Resolve the promise with a success message
    resolve("Success!");
  }, 4000); // Delay of 4 seconds
});

// Handle the resolved promise
promiseSuccess.then(result => console.log(result));
