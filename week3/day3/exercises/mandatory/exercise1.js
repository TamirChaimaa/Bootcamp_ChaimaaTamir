//Create a function call displayNumbersDivisible() that takes no parameter.
function  displayNumbersDivisible(divisor){
    sum = 0;
    //In the function, loop through numbers 0 to 500.
    for(let i=0;i<=500;i++){
        if(i%divisor===0){
            console.log(i);
            sum+=i;
        }
    }
     console.log(sum);

}
 displayNumbersDivisible(23);
