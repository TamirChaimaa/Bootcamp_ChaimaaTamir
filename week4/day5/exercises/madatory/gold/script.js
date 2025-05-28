let board = Array(9).fill('');
let playerSymbol = '';
let computerSymbol = '';
let gameOver = false;

const winCombos = [
  [0,1,2], [3,4,5], [6,7,8],
  [0,3,6], [1,4,7], [2,5,8],
  [0,4,8], [2,4,6]
];

function chooseSymbol(symbol) {
  playerSymbol = symbol;
  computerSymbol = symbol === 'X' ? 'O' : 'X';
  board = Array(9).fill('');
  gameOver = false;
  document.querySelectorAll('.cell').forEach(cell => cell.textContent = '');
  document.getElementById('message').textContent = '';
  document.getElementById('restart').style.display = 'none';
  if (computerSymbol === 'X') computerMove();
}

function playerTurn(index) {
  if (gameOver || board[index] !== '') return;
  board[index] = playerSymbol;
  document.getElementById(index).textContent = playerSymbol;
  if (checkWinner(playerSymbol)) return;
  if (board.every(cell => cell !== '')) return endGame("Tie Game!");
  computerMove();
}

function computerMove() {
  if (gameOver) return;
  const difficulty = document.getElementById('difficulty').value;
  let move;

  if (difficulty === 'easy') {
    let empty = board.map((v, i) => v === '' ? i : null).filter(v => v !== null);
    move = empty[Math.floor(Math.random() * empty.length)];
  } else {
    move = getBestMove();
  }

  board[move] = computerSymbol;
  document.getElementById(move).textContent = computerSymbol;
  if (checkWinner(computerSymbol)) return;
  if (board.every(cell => cell !== '')) endGame("Tie Game!");
}

function checkWinner(symbol) {
  for (let combo of winCombos) {
    if (combo.every(i => board[i] === symbol)) {
      endGame(`${symbol} wins!`);
      return true;
    }
  }
  return false;
}

function endGame(message) {
  gameOver = true;
  document.getElementById('message').textContent = message;
  document.getElementById('restart').style.display = 'inline-block';
}

function restartGame() {
  chooseSymbol(playerSymbol);
}

// Minimax strategy (simplified for blocking/winning)
function getBestMove() {
  // 1. Win if possible
  for (let i = 0; i < 9; i++) {
    if (board[i] === '') {
      board[i] = computerSymbol;
      if (checkWinner(computerSymbol)) {
        board[i] = '';
        return i;
      }
      board[i] = '';
    }
  }
  // 2. Block player win
  for (let i = 0; i < 9; i++) {
    if (board[i] === '') {
      board[i] = playerSymbol;
      if (checkWinner(playerSymbol)) {
        board[i] = '';
        return i;
      }
      board[i] = '';
    }
  }
  // 3. Pick center
  if (board[4] === '') return 4;
  // 4. Pick random
  let empty = board.map((v, i) => v === '' ? i : null).filter(v => v !== null);
  return empty[Math.floor(Math.random() * empty.length)];
}
