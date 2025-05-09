# Game board initialization
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to get player input
def player_input(player, board):
    while True:
        try:
            choice = int(input(f"Player {player}, enter a number (1-9) for your move: ")) - 1
            if choice < 0 or choice > 8 or board[choice] != ' ':
                print("Invalid move, try again.")
            else:
                board[choice] = player
                break
        except ValueError:
            print("Please enter a valid number.")
    
# Check for a win
def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
        
    return None

# Main function
def play():
    board = [' '] * 9  # Empty board
    current_player = 'X'
    while True:
        display_board(board)
        player_input(current_player, board)
        winner = check_win(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            break
        if ' ' not in board:
            display_board(board)
            print("It's a draw!")
            break
        current_player = 'O' if current_player == 'X' else 'X'

play()





