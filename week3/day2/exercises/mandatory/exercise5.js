let  family = {
  father: "John",
  mother: "Jane",
  son: "Mike",
  daughter: "Emily",
  pet: "Buddy"
};

//Using a for in loop, console.log the keys of the object.
for (let key in family) {
  console.log(key);
}
//Using a for in loop, console.log the values of the object.
for (let key in family) {
  console.log(family[key]);
}