#Exercise 4: Check the index
#Using this variable:
#names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#Ask a user for their name, if their name is in the names list print out the index of the first occurrence of the name.
#Example: if input is Cortana we should be printing the index 1
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
# Convert all names in the list to uppercase
for i in range(len(names)):
    names[i] = names[i].upper()
name = input("Enter your name: ")
name=name.upper()
if name in names:
    print("Your name is at index", names.index(name))
else:
    print("Your name is not in the list.")