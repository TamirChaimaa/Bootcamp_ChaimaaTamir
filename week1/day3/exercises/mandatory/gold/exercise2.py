#Exercise 2 : Custom List Class
#Instructions
#Create a class called MyList, the class should receive a list of letters.
#Add a method that returns the reversed list.
#Add a method that returns the sorted list.
#Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).Bonus : Create a method that generates a second list with the same length as mylist. The list should be constructed with random numbers. (use list comprehension).
import random

class MyList:
    def __init__(self, letters):
        self.list = letters
    
    def reverse_list(self):
        return self.list[::-1]
    
    def sort_list(self):
        return sorted(self.list)
    
    def random_list(self):
        return [random.randint(1, 100) for _ in range(len(self.list))]

if __name__ == "__main__":
    my_list = MyList(['a', 'b', 'c', 'd', 'e'])

print(f"Original list: {my_list.list}")
print(f"Reversed list: {my_list.reverse_list()}")
print(f"Sorted list: {my_list.sort_list()}")
print(f"Random list of the same length: {my_list.random_list()}")
