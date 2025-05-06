#Exercise 1: What is the Season?
#Ask the user to input a month (1 to 12).
#Display the season of the month received:
#Spring runs from March (3) to May (5)
#Summer runs from June (6) to August (8)
#Autumn runs from September (9) to November (11)
#Winter runs from December (12) to February (2)

# Ask the user to input a month number (from 1 to 12)
month = int(input("Enter a month number (1 to 12): "))

# Check the season based on the month
if month == 3 or month == 4 or month == 5:
    print("Spring")
elif month == 6 or month == 7 or month == 8:
    print("Summer")
elif month == 9 or month == 10 or month == 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    # If the user enters an invalid month number
    print("Please enter a valid month number (1 to 12).")
