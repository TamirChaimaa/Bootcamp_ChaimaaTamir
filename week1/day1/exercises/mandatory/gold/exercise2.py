#Exercise 2: For Loop
#Use a for loop to print all numbers from 1 to 20, inclusive.
#Using a for loop, that loops from 1 to 20 (inclusive), print out every element which has an even index.
for number in range(1, 21):  
    print(number)  
print("#################################################")
###################################################
numbers = list(range(1, 21))
for i in range(len(numbers)):  
    if i % 2 == 0:  
        print(numbers[i])
