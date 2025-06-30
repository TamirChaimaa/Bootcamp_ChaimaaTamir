function multiplyProperty(obj, key, factor) {
    return obj[key] * factor;
}
var product1 = {
    price: 100,
    quantity: 5,
};
var product2 = {
    length: 20,
    width: 10,
};
console.log(multiplyProperty(product1, "price", 2));
console.log(multiplyProperty(product1, "quantity", 3));
console.log(multiplyProperty(product2, "length", 4));
console.log(multiplyProperty(product2, "width", 5));
