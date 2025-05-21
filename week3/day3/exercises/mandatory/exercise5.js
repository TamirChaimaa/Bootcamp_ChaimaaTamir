// 1. Get the div with id "container" and log it to the console
let containerDiv = document.getElementById('container');
console.log('Step 1 - container div:', containerDiv);

// 2. Change the name "Pete" to "Richard"
let firstList = document.querySelectorAll('ul.list')[0];
let peteLi = firstList.querySelectorAll('li')[1];
console.log('Step 2 - before change:', peteLi.textContent);
peteLi.textContent = 'Richard';
console.log('Step 2 - after change:', peteLi.textContent);

// 3. Remove the second <li> from the second <ul>
let secondList = document.querySelectorAll('ul.list')[1];
let secondLiSecondList = secondList.querySelectorAll('li')[1];
console.log('Step 3 - item to remove:', secondLiSecondList.textContent);
secondList.removeChild(secondLiSecondList);
console.log('Step 3 - second <ul> after removal:', secondList.innerHTML);

// 4. Change the name of the first <li> in each <ul> to your name (example: "Chaimaa")
let lists = document.querySelectorAll('ul.list');
lists.forEach((ul, index) => {
  let firstLi = ul.querySelector('li');
  console.log(`Step 4 - before change in list ${index + 1}:`, firstLi.textContent);
  firstLi.textContent = 'Chaimaa';
  console.log(`Step 4 - after change in list ${index + 1}:`, firstLi.textContent);
});


// part3
//Add a class called student_list to both of the <ul>'
let all_elements_ul = document.querySelectorAll('ul');
console.log(all_elements_ul);
all_elements_ul.forEach(ul => {
  ul.classList.add('student_list');
  console.log(ul);
});

// Add class "university" and "attendance" to the first <ul>
all_elements_ul[0].classList.add('university', 'attendance');
console.log(all_elements_ul[0]);

//part4
//Add a “light blue” background color and some padding to the <div>.
 containerDiv.style.backgroundColor = 'lightblue';

//Do not display the <li> that contains the text node “Dan”. (the last <li> of the first <ul>)
let firstListLi = firstList.querySelectorAll('li');
firstListLi[firstListLi.length - 1].style.display = 'none';
console.log(firstListLi[firstListLi.length - 1]);

//Add a border to the <li> that contains the text node “Richard”. (the second <li> of the <ul>)
let secondListLi = secondList.querySelectorAll('li');
secondListLi[1].style.border = '1px solid black';
console.log(secondListLi[1]);

//Change the font size of the whole body.
document.body.style.fontSize = '20px';

//Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

if (containerDiv.style.backgroundColor === 'lightblue') {
  alert('Hello Chaimaa and Sarah');
}