function getProperty<T>(obj: T, key: keyof T) {
    return obj[key];
}

const user = {
    name: "Alice",
    age: 25,
    isAdmin: false,
};

console.log(getProperty(user, "name"));
console.log(getProperty(user, "age"));
console.log(getProperty(user, "isAdmin")); 
