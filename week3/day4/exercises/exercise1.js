parent_article = document.querySelector("article");
child_h1 = parent_article.querySelector("h1");
console.log(child_h1);
//Using DOM methods, remove the last paragraph in the <article> tag.
parent_article.removeChild(parent_article.lastElementChild);
console.log(parent_article);

//Add a event listener which will change the background color of the h2 to red, when it’s clicked on.
parent_article.querySelector("h2").addEventListener("click", () => {
    parent_article.querySelector("h2").style.backgroundColor = "red";
})

parent_article.querySelector("h3").addEventListener("click", () => {
   parent_article.querySelector("h3").hidden = true;
})
//Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.
parent_article.querySelector("button").addEventListener("click", () => {
  const paragraphs = parent_article.querySelectorAll("p");

  paragraphs.forEach(p => {
    p.style.fontWeight = "bold";
  });
})

//BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)
parent_article.querySelector("h1").addEventListener("mouseover", () => {
    const randomSize = Math.floor(Math.random() * 100);
    parent_article.querySelector("h1").style.fontSize = `${randomSize}px`;

})



