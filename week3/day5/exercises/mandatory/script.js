// Get the element with the ID 'grid' from the HTML.
// This is where the cells (pixels) will be placed.
const grid = document.getElementById('grid');

// Get the button with the ID 'clear' to clear the grid later.
const clearButton = document.getElementById('clear');

// Get all the elements with the class 'color'.
// These will be used to select a drawing color.
const colorElements = document.querySelectorAll('.color');

// Set the default drawing color to black.
let currentColor = 'black';

// This variable will help us know if the mouse button is being held down.
let isDrawing = false;

// Create 50 * 30 = 1500 cells for the grid.
for (let i = 0; i < 50 * 30; i++) {
  // Create a new div element (this will be a cell).
  const cell = document.createElement('div');

  // Add the class 'cell' to the div for styling.
  cell.classList.add('cell');

  // Add the cell to the grid in the HTML.
  grid.appendChild(cell);

  // When the mouse is clicked down on a cell,
  // change the cell's color and set isDrawing to true.
  cell.addEventListener('mousedown', () => {
    cell.style.backgroundColor = currentColor;
    isDrawing = true;
  });

  // When the mouse moves over a cell and the mouse is held down,
  // also change the cell's color.
  cell.addEventListener('mouseover', () => {
    if (isDrawing) {
      cell.style.backgroundColor = currentColor;
    }
  });

  // When the mouse button is released over a cell,
  // stop drawing by setting isDrawing to false.
  cell.addEventListener('mouseup', () => {
    isDrawing = false;
  });
}

// This makes sure that drawing stops even if the mouse is released
// outside of a cell.
document.addEventListener('mouseup', () => {
  isDrawing = false;
});

// For each color option in the color palette:
colorElements.forEach(color => {
  // When a color is clicked, update the current drawing color
  // to the one that was clicked.
  color.addEventListener('click', () => {
    currentColor = color.style.backgroundColor;
  });
});

// When the clear button is clicked:
clearButton.addEventListener('click', () => {
  // Go through each cell and reset its background color to white.
  document.querySelectorAll('.cell').forEach(cell => {
    cell.style.backgroundColor = 'white';
  });
});
