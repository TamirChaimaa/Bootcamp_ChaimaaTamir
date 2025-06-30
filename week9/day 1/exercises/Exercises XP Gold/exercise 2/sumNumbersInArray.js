function sumNumbersInArray(arr) {
    var sum = 0;
    for (var _i = 0, arr_1 = arr; _i < arr_1.length; _i++) {
        var element = arr_1[_i];
        if (typeof element === "number") {
            sum += element;
        }
    }
    return sum;
}
console.log(sumNumbersInArray([1, 2, "3", 4]));
console.log(sumNumbersInArray(["5", "test", 10, 20]));
console.log(sumNumbersInArray(["a", "b", "c"]));
console.log(sumNumbersInArray([100, 200, 300]));
