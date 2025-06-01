// Resolve with the value 3
Promise.resolve(3)
  .then(value => console.log("Resolved with:", value));

// Reject with "Boo!"
Promise.reject("Boo!")
  .catch(error => console.log("Rejected with:", error));
