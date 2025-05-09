#Challenge 1 : Sorting
#nstructions
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Use List Comprehension
#Example:

#Suppose the following input is supplied to the program: without,hello,bag,world
#Then, the output should be: bag,hello,without,world
user_input_sequence = input("Enter a comma-separated sequence of words: ")
words = [word.strip() for word in user_input_sequence.split(",")]
sorted_words = sorted(words)
result = ", ".join(sorted_words)
print(result)