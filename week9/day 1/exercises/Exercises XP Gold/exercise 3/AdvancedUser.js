function introduceAdvancedUser(user) {
    var message = "hello, my name is ".concat(user.name, " and I am ").concat(user.age, " years old.");
    if (user.address) {
        message += " i live at ".concat(user.address, ".");
    }
    return message;
}
var user1 = {
    name: "imane",
    age: 21,
    address: "123 idk",
};
var user2 = {
    name: "ayman",
    age: 23,
};
console.log(introduceAdvancedUser(user1));
console.log(introduceAdvancedUser(user2));
