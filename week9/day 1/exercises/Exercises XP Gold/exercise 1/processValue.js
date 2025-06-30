function processValue(value) {
    if (typeof value === "number") {
        return "$".concat(value.toFixed(2));
    }
    else {
        return value.split("").reverse().join("");
    }
}
// Test the function with different inputs
console.log(processValue(100));
console.log(processValue(45.678));
console.log(processValue("hello"));
console.log(processValue("123abc"));
