function sumNumbersInArray(arr: (number | string)[]): number {
    let sum = 0;

    for (const element of arr) {
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
