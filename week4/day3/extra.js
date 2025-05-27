const object1 = {
  a: 'somestring',
  b: 42,
  c: false
};

console.log(Object.keys(object1));
Object.keys(object1).forEach(key => {
  console.log(`key: ${key}, value: ${object1[key]}`);
});