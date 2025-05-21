// Step 1: Create the allBooks array with 2 books
const allBooks = [
  {
    title: "The Hobbit",
    author: "J.R.R. Tolkien",
    image: "https://upload.wikimedia.org/wikipedia/en/4/4a/TheHobbit_FirstEdition.jpg",
    alreadyRead: true
  },
  {
    title: "1984",
    author: "George Orwell",
    image: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQNSwbp-Tpq7ox9Hsvk55ge7oEhhroHqhr64Q&s",
    alreadyRead: false
  }
];

// Step 2: Select the section where books will be rendered
const listBooksSection = document.querySelector(".listBooks");

// Step 3: Loop through each book and render it
allBooks.forEach(book => {
  // Create a div for the book
  const bookDiv = document.createElement("div");

  // Create the text node for title and author
  const bookText = document.createElement("p");
  bookText.textContent = `${book.title} written by ${book.author}`;
  
  // If the book is already read, make the text red
  if (book.alreadyRead) {
    bookText.style.color = "red";
  }

  // Create the image element
  const bookImage = document.createElement("img");
  bookImage.src = book.image;
  bookImage.style.width = "100px";

  // Append text and image to the book div
  bookDiv.appendChild(bookText);
  bookDiv.appendChild(bookImage);

  // Append the book div to the section
  listBooksSection.appendChild(bookDiv);
});
