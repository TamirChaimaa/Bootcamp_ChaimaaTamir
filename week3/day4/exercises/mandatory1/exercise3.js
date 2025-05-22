// Declare an array to store all <strong> elements
let allBoldItems = [];

// Function to get all <strong> elements and store them in allBoldItems
function getBoldItems() {
    const boldItems = document.querySelectorAll("strong"); // Select all <strong> elements in the document
    console.log(boldItems); // Log them for debugging
    allBoldItems = Array.from(boldItems); // Convert NodeList to an array and store it
}

// Function to highlight all bold items by changing their color to blue
function highlight() {
    bottomItemColor("blue");
}

// Function to reset all bold items to their default color (black)
function returnItemsToDefault() {
    bottomItemColor("black");
}

// Helper function to change the color of all bold items
function bottomItemColor(color) {
    allBoldItems.forEach(element => {
        element.style.color = color; // Set the color style of each element
    });
}

// Call the function to initialize allBoldItems
getBoldItems();

// Add event listeners to each bold item to handle mouseover and mouseout
allBoldItems.forEach(element => {
    element.addEventListener("mouseover", highlight); // Change color to blue when hovered
    element.addEventListener("mouseout", returnItemsToDefault); // Reset color when not hovered
});


       



 

