//Get a random number between 1 and 100.
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

let random_number = getRandomInt(1, 100);
console.log(random_number);
 
function even_number(){
  for(let i=0; i<=random_number; i++){
    if (i % 2 === 0) {
        console.log(i + " is even");
    }
}
}
even_number();