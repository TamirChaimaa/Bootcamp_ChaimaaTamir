const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 
//Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.
const shoppingList = ["banana", "orange", "apple"];
//Create a function called myBill() that takes no parameters.
function myBill() {
    let total = 0;

    for (let item of shoppingList) {
        if (item in stock) {
            total += prices[item];
            stock[item]--;
            if (stock[item]<0) {
                stock[item] = 0;
            }
        }
    }
    console.log(total);
}

myBill();
console.log(stock);