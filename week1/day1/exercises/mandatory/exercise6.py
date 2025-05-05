#🌟 Exercise 6: Tuple
#Given a tuple which value is integers, is it possible to add more integers to the tuple?
# Original tuple
tuple = (1, 2, 3)
print("Original tuple:", tuple)
print("Explanation: This is the original tuple, which contains the values (1, 2, 3). Tuples are immutable.")

# Attempting to use add() on a tuple (will raise an error)
try:
    # Trying to add an element to the tuple, which will result in an error since tuples are immutable
    print("Attempting to use the 'add()' method on a tuple:")
    tuple.add(6)
except AttributeError as e:
    # This will catch the error and print an explanation
    print(f"Error: {e}")
    print("Explanation: Tuples do not have the 'add()' method because they are immutable. This results in an AttributeError.")

# New integers to add
integers = (4, 5)
print("\nNew integers to add:", integers)
print("Explanation: We want to add these integers (4, 5) to the original tuple, but since tuples are immutable, we will create a new one by concatenation.")

# Create a new tuple by concatenating the original tuple and the new integers
my_tuple = tuple + integers
print("\nNew tuple after concatenation:", my_tuple)
print("Explanation: The new tuple is created by concatenating the original tuple (1, 2, 3) with the new tuple (4, 5). The result is (1, 2, 3, 4, 5).")

# Display the final result
print("\nFinal Result:")
print("New tuple:", my_tuple)
