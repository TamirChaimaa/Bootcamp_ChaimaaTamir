// The resullt is ____/''''\____ because flat is being called first, then mountain, and finally flat again.

let landscape = () => {

 let result = "";

 let flat = (x) => {
   for(let count = 0; count<x; count++){
     result = result + "_";
   }
 }

 let mountain = (x) => {
   result = result + "/"
   for(let counter = 0; counter<x; counter++){
     result = result + "'"
   }
   result = result + "\\"
 }

 flat(4);
 mountain(4);
 flat(4)

 return result;
}
landscape()
// console.log(landscape())