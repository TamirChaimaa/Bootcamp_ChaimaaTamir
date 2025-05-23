const grid = document.getElementById('grid');
const clearButton = document.getElementById('clear');
const colorElements = document.querySelectorAll('.color');

let currentColor = 'black';
let isDrawing = false;

// Create grid
for (let i = 0; i < 50 * 30; i++) {
  const cell = document.createElement('div');
  cell.classList.add('cell');
  grid.appendChild(cell);

  cell.addEventListener('mousedown', () => {
    cell.style.backgroundColor = currentColor;
    isDrawing = true;
  });

  cell.addEventListener('mouseover', () => {
    if (isDrawing) {
      cell.style.backgroundColor = currentColor;
    }
  });

  cell.addEventListener('mouseup', () => {
    isDrawing = false;
  });
}

// Track mouse up globally to stop drawing
document.addEventListener('mouseup', () => {
  isDrawing = false;
});

// Handle color selection
colorElements.forEach(color => {
  color.addEventListener('click', () => {
    currentColor = color.style.backgroundColor;
  });
});

// Clear grid
clearButton.addEventListener('click', () => {
  document.querySelectorAll('.cell').forEach(cell => {
    cell.style.backgroundColor = 'white';
  });
});
