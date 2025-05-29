    const winCombos = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [6, 4, 2]
    ];

    let board = Array(9).fill(null);
    let playerSymbol = 'X';
    let computerSymbol = 'O';
    let gameActive = true;

    function chooseSymbol(symbol) {
      playerSymbol = symbol;
      computerSymbol = symbol === 'X' ? 'O' : 'X';
      startGame();
    }

    function startGame() {
      board = Array(9).fill(null);
      gameActive = true;
      document.getElementById('message').textContent = '';
      document.getElementById('restartBtn').style.display = 'none';
      renderBoard();
    }

    function renderBoard() {
      const boardEl = document.getElementById('board');
      boardEl.innerHTML = '';
      board.forEach((val, idx) => {
        const cell = document.createElement('div');
        cell.classList.add('cell');
        cell.id = 'cell-' + idx;
        cell.textContent = val || '';
        cell.addEventListener('click', () => makeMove(idx));
        boardEl.appendChild(cell);
      });
    }

    function makeMove(index) {
      if (!gameActive || board[index]) return;
      board[index] = playerSymbol;
      updateBoard();
      if (checkWinner(playerSymbol)) return;
      if (board.every(cell => cell)) return endGame("It's a tie!");
      setTimeout(computerMove, 300);
    }

    function computerMove() {
      const difficulty = document.getElementById('difficulty').value;
      let index;
      if (difficulty === 'easy') {
        const empty = board.map((val, idx) => val ? null : idx).filter(v => v !== null);
        index = empty[Math.floor(Math.random() * empty.length)];
      } else {
        index = bestMove();
      }
      if (index !== undefined) {
        board[index] = computerSymbol;
        updateBoard();
        if (checkWinner(computerSymbol)) return;
        if (board.every(cell => cell)) return endGame("It's a tie!");
      }
    }

    function updateBoard() {
      board.forEach((val, idx) => {
        document.getElementById('cell-' + idx).textContent = val;
      });
    }

    function checkWinner(symbol) {
      const plays = board.map((val, idx) => val === symbol ? idx : -1).filter(v => v !== -1);
      const winner = winCombos.some(combo => combo.every(index => plays.includes(index)));
      if (winner) {
        endGame(symbol === playerSymbol ? 'You win!' : 'Computer wins!');
        return true;
      }
      return false;
    }

    function endGame(message) {
      gameActive = false;
      document.getElementById('message').textContent = message;
      document.getElementById('restartBtn').style.display = 'block';
    }

    function bestMove() {
      for (let combo of winCombos) {
        const [a, b, c] = combo;
        const line = [board[a], board[b], board[c]];

        if (line.filter(v => v === computerSymbol).length === 2 && line.includes(null)) {
          return combo[line.indexOf(null)];
        }

        if (line.filter(v => v === playerSymbol).length === 2 && line.includes(null)) {
          return combo[line.indexOf(null)];
        }
      }
      const empty = board.map((val, idx) => val ? null : idx).filter(v => v !== null);
      return empty[Math.floor(Math.random() * empty.length)];
    }