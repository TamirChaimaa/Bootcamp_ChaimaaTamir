#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
string = input("Enter a string: ")
result = ""
for char in string:
    if char not in result:
        result += char
print(result)