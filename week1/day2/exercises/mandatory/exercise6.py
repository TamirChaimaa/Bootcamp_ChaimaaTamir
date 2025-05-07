#🌟 Exercise 6 : Let’s create some personalized shirts !
# Define the function
def make_shirt(size, message):
    print(f"The size of the shirt is {size} and the text is '{message}'")
make_shirt("Small", "Python is awesome!")

#Redefine the function with default values
def make_shirt(size="Large", message="I love Python"):
    print(f"The size of the shirt is {size} and the text is '{message}'")
make_shirt()

#Call the function, in order to make a large shirt with the default message
make_shirt(size="Large")

# Medium shirt with the default message
make_shirt(size="Medium")

# Any size shirt with a custom message
make_shirt(size="Small", message="Code is life!")

# Call the function using keyword arguments 
make_shirt(message="Keep calm and code on", size="XLL")
