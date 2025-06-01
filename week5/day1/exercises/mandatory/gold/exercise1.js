// Declare the promises
const promise1 = Promise.resolve(3);
const promise2 = 42; // This is not a Promise, but Promise.all will wrap it in a resolved Promise automatically
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'foo'); // Resolves after 3 seconds with the value 'foo'
});

// Use Promise.all to wait for all promises to resolve
Promise.all([promise1, promise2, promise3])
  .then((values) => {
    console.log(values); // Expected output: [3, 42, "foo"]
  })
  .catch((error) => {
    console.error("One of the promises failed:", error);
  });

/*
Explanation:
- Promise.all takes an array of promises and returns a single Promise.
- This returned Promise resolves when **all** of the input promises have resolved.
- The result is an array of resolved values, in the same order as the input.
- If **any** promise is rejected, Promise.all immediately rejects with that reason.
- In this example:
    - promise1 resolves immediately with 3
    - promise2 is a number (not a Promise), so Promise.all treats it as Promise.resolve(42)
    - promise3 resolves after 3 seconds with "foo"
- Therefore, after 3 seconds, the final output is: [3, 42, "foo"]
*/
