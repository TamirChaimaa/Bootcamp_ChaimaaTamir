const people = ["Greg", "Mary", "Devon", "James"];
// Write code to remove “Greg” from the people array.
people.splice(people.indexOf( "Greg"), 1);
console.log(people);

//Write code to replace “James” to “Jason”.
index_of_james = people.indexOf("James");
people[index_of_james] = "Jason";
console.log(people);

//Write code to add your name to the end of the people array.
people.push("Chaimaa");
console.log(people);

//Write code that console.logs Mary’s index. 
console.log(people.indexOf("Mary"));

//Write code to make a copy of the people array using the slice method.	
const sub_people= people.slice(1, 5);
console.log(sub_people);

//Write code that gives the index of “Foo”. Why does it return -1 ?
console.log(people.indexOf("Foo"));
// because Foo is not in the array

 last =people[people.length-1];
 console.log(last);

//Part II - Loops

//Using a loop, iterate through the people array and console.log each person.
for(let i=0;i<people.length;i++){
  console.log(people[i]);
}

//Using a loop, iterate through the people array and exit the loop after you console.log “Devon” .
for(let i=0;i<people.length;i++){
  console.log(people[i]);
  if(people[i]==="Devon"){
    break;
  }
}