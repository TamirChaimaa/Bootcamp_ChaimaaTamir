#Challenge 1
# Ask the user for a number and a length.
#Create a program that prints a list of multiples of the number until the list length reaches length.
number = int(input("Enter a number: "))
length = int(input("Enter a length: "))
result = []
for i in range(1, length + 1):
    result.append(number * i)
print(result)