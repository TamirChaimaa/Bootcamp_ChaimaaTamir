function welcomeUser(name, greeting) {
    if (greeting === void 0) { greeting = "Hello"; }
    return "".concat(greeting, ", ").concat(name, "!");
}
console.log(welcomeUser("imane"));
console.log(welcomeUser("ayman", "Welcome"));
console.log(welcomeUser("sanaa", "Good day"));
