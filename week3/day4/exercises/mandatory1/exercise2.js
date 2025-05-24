  // Retrieve the form and log it to the console
  const form = document.querySelector('form');
  console.log('Form:', form);

  // Retrieve the inputs by their id and log them
  const inputFname = document.getElementById('fname');
  const inputLname = document.getElementById('lname');
  console.log('Inputs by id:', inputFname, inputLname);

  // Retrieve the inputs by their name attribute and log them
  const inputByNameFname = document.querySelector('input[name="firstname"]');
  const inputByNameLname = document.querySelector('input[name="lastname"]');
  console.log('Inputs by name:', inputByNameFname, inputByNameLname);

  // Select the <ul> element with class "usersAnswer" where the answers will be shown
  const usersAnswerList = document.querySelector('.usersAnswer');

  // Add a submit event listener to the form
  form.addEventListener('submit', function(event) {
    // Use event.preventDefault() to stop the form from submitting and reloading the page
    event.preventDefault();

    // Clear the <ul> content before adding new answers to avoid duplicates
    usersAnswerList.innerHTML = '';

    // Get the trimmed values of the input fields
    const firstNameValue = inputFname.value.trim();
    const lastNameValue = inputLname.value.trim();

    // Check that the input values are not empty
    if (firstNameValue === '' || lastNameValue === '') {
      alert('Please fill in both fields.');
      return; // Stop the function if either input is empty
    }

    // Create an <li> element for the first name and set its text content
    const liFirstName = document.createElement('li');
    liFirstName.textContent = firstNameValue;

    // Create an <li> element for the last name and set its text content
    const liLastName = document.createElement('li');
    liLastName.textContent = lastNameValue;

    // Append the <li> elements to the <ul> below the form
    usersAnswerList.appendChild(liFirstName);
    usersAnswerList.appendChild(liLastName);

    // Optional: reset the form inputs after submission
    form.reset();
  });