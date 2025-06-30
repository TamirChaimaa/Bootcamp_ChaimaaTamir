function checkNumber(num) {
    if (num > 0) {
        return 'the number is positive';
    }
    else if (num < 0) {
        return 'the number is negative';
    }
    else {
        return 'the number is zero';
    }
}
console.log(checkNumber(10));
console.log(checkNumber(-5));
console.log(checkNumber(0));
