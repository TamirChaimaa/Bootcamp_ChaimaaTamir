#Instructions
#Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
#Display a little cake as seen below:
#___iiiii___
#|:H:a:p:p:y:|
#__|___________|__
#|^^^^^^^^^^^^^^^^^|
#|:B:i:r:t:h:d:a:y:|
#|                 |
#~~~~~~~~~~~~~~~~~~~
#The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
#Bonus : If they were born on a leap year, display two cakes !
# Import the modules needed to work with dates and leap years
from datetime import datetime
import calendar

# Ask the user to enter their birthdate in the format DD/MM/YYYY
birthdate_str = input("Enter your birthdate (format DD/MM/YYYY): ")

# Convert the input (a string) into a real date
birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y")

# Get today’s date
today = datetime.today()

# Calculate the age by subtracting the birth year from the current year
age = today.year - birthdate.year

# Check if the birthday hasn’t happened yet this year
# If it hasn’t, subtract 1 from the age
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Get the last digit of the age (for example, 53 → 3)
candles_count = age % 10

# Make that many candle letters ("i") for the cake top
candles = "i" * candles_count
print(f"       ___{candles}___")
print("      |:H:a:p:p:y:|")
print("    __|___________|__")
print("   |^^^^^^^^^^^^^^^^^|")
print("   |:B:i:r:t:h:d:a:y:|")
print("   |                 |")
print("   ~~~~~~~~~~~~~~~~~~~")

# BONUS: If the user was born in a leap year, show a second cake!
if calendar.isleap(birthdate.year):
    print("\nLeap year bonus! You get another cake!\n")
    print(f"       ___{candles}___")
    print("      |:H:a:p:p:y:|")
    print("    __|___________|__")
    print("   |^^^^^^^^^^^^^^^^^|")
    print("   |:B:i:r:t:h:d:a:y:|")
    print("   |                 |")
    print("   ~~~~~~~~~~~~~~~~~~~")
