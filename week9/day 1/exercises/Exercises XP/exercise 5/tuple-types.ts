function getDetails(name:string , age : number) : [string, number, string] {
    const greeting = `Hello, ${name}! You are ${age} years old.`;
    return [name , age , greeting];
}   

const details = getDetails ('imane' , 21);
console.log(details);
