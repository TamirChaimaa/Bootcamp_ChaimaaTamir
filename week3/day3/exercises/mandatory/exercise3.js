function changeEnough(itemPrice, amountOfChange){
    sum=0
    quarter = 0.25 * amountOfChange[0]
    dime = 0.10 * amountOfChange[1]
    nickel = 0.05 * amountOfChange[2]
    penny = 0.01 * amountOfChange[3]
    amountOfChange = [quarter, dime, nickel, penny]
    for (let i = 0; i < amountOfChange.length; i++) {
        sum += amountOfChange[i]
    }
    if (itemPrice <= sum) {
        return true;
    }else {
        return false;
    }
}
console.log(changeEnough(4.25, [25, 20, 5, 0]))
console.log(changeEnough(0.75, [0,0,20,5]))
console.log(changeEnough(14.11, [2,100,0,0]))