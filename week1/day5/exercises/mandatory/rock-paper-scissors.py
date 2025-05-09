from game import Game
 
def get_user_menu_choice():
    #- this should display a simple menu, get the user’s choice (with data validation), and return the choice. No looping should occur here.
    #The possibles choices are : Play a new game or Show scores or Quit
    print("\nMenu:")
    print("g Play a new game")
    print("s Show scores until now")
    print("q show scores and quit")
    
    choice = input("Enter your choice: ").lower()
    if choice not in ['g','s','q']:
        choice = input("Enter your choice: ").lower()
    return choice
    

def print_results(results):
    #this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.
    #Note: results should be in this form: {win: 2,loss: 4,draw: 3}. Bear in mind that this dictionary will need to be created and populated in some other part of our code, and passed in to the print_results function at the right time.
    print("\nGame Results Summary:")
    print(f"Wins: {results['win']},Losses: {results['loss'] },Draws: {results['draw']}")
    print("Thank you for playing!")


def main():
    #main() - the main function. It should take care of 3 things:
    #Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’, whatever you decide. (Make use of the get_user_menu_choice function)

     
    #When the user chooses to play a game:
    #Create a new Game object (see below), and call its play() function, receiving the result of the game that is returned.
    #Remember the results of every game that is played.


    #When the user chooses to exit the program, call the print_results function in order to display a summary of all the games played.
    game = Game()
    results = {'win': 0, 'loss': 0, 'draw': 0}
    
    while True:
        choice = get_user_menu_choice()
        
        if choice == 'g':
            result = game.play()
            if result == 'win':
                results['win'] += 1
            elif result == 'loss':
                results['loss'] += 1
            else:
                results['draw'] += 1
        
        elif choice == 's':
            print_results(results)
        
        elif choice == 'q':
            print_results(results)
            break

main()
