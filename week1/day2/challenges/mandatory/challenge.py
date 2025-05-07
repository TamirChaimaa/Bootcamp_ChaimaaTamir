#Ask a user for a word.

user_word = input("Please enter a word:")
#Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
word_dict={}
#Make sure the letters are the keys.
#Make sure the letters are strings.
#Make sure the indexes are stored in a list, and those lists are values.
for i in range(len(user_word)):
    if user_word[i] in word_dict.keys():
        word_dict[user_word[i]].append(i)
    else:
        word_dict[user_word[i]]=[i]

print(word_dict)
#enumerate index vale 
