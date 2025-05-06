#Exercise 3: While Loop
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
name = input("What's your name? ")
name = name.lower()
while name != "chaimaa":
    name = input("What's your name? ")