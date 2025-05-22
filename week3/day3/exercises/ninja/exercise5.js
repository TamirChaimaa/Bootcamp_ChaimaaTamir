
function getUniqueElements(arr) {
  let unique = [];
  for (let i = 0; i < arr.length; i++) {
    if (!unique.includes(arr[i])) {
      unique.push(arr[i]);
    }
  }
  return unique;
}

let list = [1, 2, 3, 3, 3, 3, 4, 5];
let newList = getUniqueElements(list);

console.log(newList); 
