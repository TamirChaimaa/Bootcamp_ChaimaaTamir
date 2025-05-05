#Exercise 5: Greatest Number
#Ask the user for 3 numbers and print the greatest number.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
greatest_number = number1
if number2 > greatest_number:
    greatest_number = number2
if number3 > greatest_number:
    greatest = number3
print("The greatest number is :", greatest)