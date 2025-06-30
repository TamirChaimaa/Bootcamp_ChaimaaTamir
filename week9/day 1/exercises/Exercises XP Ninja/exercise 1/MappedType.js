function mapType(value) {
    if (typeof value === "number") {
        return value * value;
    }
    else {
        return value.length;
    }
}
console.log(mapType(4));
console.log(mapType("hello"));
