type Person = {
    name : string;
    age : number;
}

function createPerson(name:string , age : number) : Person {
    return {
        name : name,
        age : age,
    }
}

const person1 = createPerson("imane", 21);
console.log(person1);