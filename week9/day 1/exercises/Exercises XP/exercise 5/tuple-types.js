function getDetails(name, age) {
    var greeting = "Hello, ".concat(name, "! You are ").concat(age, " years old.");
    return [name, age, greeting];
}
var details = getDetails('imane', 21);
console.log(details);
