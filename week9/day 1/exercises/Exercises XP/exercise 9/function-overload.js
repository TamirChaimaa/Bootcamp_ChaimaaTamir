function greet(name) {
    if (name) {
        return "Hello, ".concat(name, "!");
    }
    else {
        return "Hello, stranger!";
    }
}
console.log(greet("imane"));
console.log(greet());
