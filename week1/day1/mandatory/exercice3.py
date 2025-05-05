#🌟 Exercise 3 : What’s your name ?
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.
# Your name
my_name = "Chaimaa"
name = input("What's your name? ")
if name.lower() == my_name.lower():
    print("Whoa! We have the same name!")
else:
    print(f"Nice to meet you, {name}! Not everyone can be as cool as {my_name}")
