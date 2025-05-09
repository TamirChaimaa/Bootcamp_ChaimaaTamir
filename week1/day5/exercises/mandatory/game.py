
import random
class Game:
    valid_items = ['rock', 'paper', 'scissors']



    # Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data validation and looping. Return the item at the end of the function.
    def get_user_item(self):
        user_item = input("Choose rock, paper, or scissors: ").lower()
        # Loop until the user enters a valid item
        while user_item not in Game.valid_items:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            user_item = input("Choose rock, paper, or scissors: ").lower()
        return user_item


    #Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s random.choice() function (read about it online).
    def get_computer_item(self):
        return random.choice(['rock', 'paper', 'scissors'])


     #Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.
    def get_game_result(self, user_item, computer_item) :
        if user_item == computer_item:
            return "draw"
        elif (user_item == 'rock' and computer_item == 'scissors') or \
             (user_item == 'paper' and computer_item == 'rock') or \
             (user_item == 'scissors' and computer_item == 'paper'):
            return "win"
        else:
            return "loss"
    #play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py
    
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(f"You selected {user_item}, The computer selected {computer_item}.  You {result}!")
        return result