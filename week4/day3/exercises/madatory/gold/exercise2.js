

function keysAndValues(obj) {
  // Get the keys and sort them alphabetically
  const keys = Object.keys(obj).sort();

  // Get the values corresponding to the sorted keys
  const values = keys.map(key => obj[key]);

  // Return an array containing keys and values arrays
  return [keys, values];
}

// Tests
console.log(keysAndValues({ a: 1, b: 2, c: 3 }));

console.log(keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" }));

console.log(keysAndValues({ key1: true, key2: false, key3: undefined }));


