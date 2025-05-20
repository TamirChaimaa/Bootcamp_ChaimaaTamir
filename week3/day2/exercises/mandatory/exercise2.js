let colors = ["blue", "green", "purple", "black", "white"];
const suffixes = ["st", "nd", "rd", "th", "th"];
for(let i=0; i<colors.length; i++){
   // console.log(`My #${i+1} is ${colors[i]}`);
    console.log(`My ${i+1}${suffixes[i]} is ${colors[i]}`);

}
