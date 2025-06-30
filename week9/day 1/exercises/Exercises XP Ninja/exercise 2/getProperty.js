function getProperty(obj, key) {
    return obj[key];
}
var user = {
    name: "Alice",
    age: 25,
    isAdmin: false,
};
console.log(getProperty(user, "name"));
console.log(getProperty(user, "age"));
console.log(getProperty(user, "isAdmin"));
