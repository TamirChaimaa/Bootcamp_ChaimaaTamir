#Exercise 2 : Longest word without a specific character
#Keep asking the user to input the longest sentence they can without the character “A”.
#Each time a user successfully sets a new longest sentence, print a congratulations message.
is_longest = False
while not is_longest:
    sentence = input("Enter a sentence: ")
    if "A" not in sentence:
        is_longest = True
        print("Well done!")
    else:
        is_longest = False
        print("Try again.")
        
