#Exercise 2: Birthdays Advanced
birthdays = {
    "Albert": "1879/03/14",
    "Marie": "1867/11/07",
    "Ada": "1815/12/10",
    "Nelson": "1918/07/18",
    "Leonardo": "1452/04/15"
}
#Before asking the user to input a person's name, print out all of the names in the dictionary.
#Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”
print(birthdays)
#Ask the user to give you a person's name and store the answer in a variable.
person_name = input("Please enter a person's name:")
#Flag
is_found = False
person_name = person_name.lower()
for name , date in birthdays.items():
    if person_name ==name.lower():
         #Print out the birthday with a nicely-formatted message.
         print(f"{name} borned on {date}")
         is_found = True
         # If the name is founded in the diactionary, we can break the loop
         break
if not is_found:
         #if the name is not found 
         print("Sorry, we don’t have the birthday information for person's name")


