#Exercise 1: Birthday Look-up
#Initialize this variable with the birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value should be their birthday. Tip: Use the format "YYYY/MM/DD".
birthdays = {
    "Albert": "1879/03/14",
    "Marie": "1867/11/07",
    "Ada": "1815/12/10",
    "Nelson": "1918/07/18",
    "Leonardo": "1452/04/15"
}
#Print a welcome message for the user. Then tell them: “You can look up the birthdays of the people in the list!”
print("You can look up the birthdays of the people in the list!")
#Ask the user to give you a person's name and store the answer in a variable.
person_name = input("Please enter a person's name:")

person_name = person_name.lower()
for name , date in birthdays.items():
    if person_name ==name.lower():
         #Print out the birthday with a nicely-formatted message.
         print(f"{name} borned on {date}")
         # If the name is founded in the diactionary, we can break the loop
         break






