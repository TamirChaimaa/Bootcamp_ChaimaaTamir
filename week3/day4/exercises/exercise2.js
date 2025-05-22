form = document.querySelector("form");
console.log(form);
//Retrieve the inputs by their id and console.log them.
form_inputs = form.querySelectorAll("input");
form_inputs.forEach(input => {
  console.log(input);
  console.log(input.id);
});


form_inputs.forEach(input => {
  console.log(input);
  console.log(input.name);
});


button_submit = form_inputs[2];
console.log(button_submit);   

button_submit.addEventListener("click", (event) => {
    event.preventDefault();
    // We use event.preventDefault() to stop the default action of an event from happening,
    // such as preventing a form from submitting or a link from navigating.
    
    form_inputs.forEach(input => {
        if(input.type === "submit") {
            return;
        }
        if(input.value === "") {
            alert("Please fill in all fields");
            return;
        }
        console.log(input);
        console.log(input.value);

        //create an li per input value,
        let li = document.createElement("li");
        li.textContent = input.value;
        let ul = document.querySelector(".usersAnswer");
        ul.appendChild(li);
   
        
    });
});





