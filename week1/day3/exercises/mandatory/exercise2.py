# Exercise 2 : Dogs
class Dog:
     def __init__(self, name, height):
         self.name = name
         self.height = height

     # Function Bark
     def bark(self):
        print(f"{self.name} goes woof!")
    
    #Function Jump
     def jump(self):
        x = self.height * 2
        print(f"{self.name} jumps {x} cm high!")

#Create davids_dog and sarahs_dog objects with their respective names and heights.
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Lassie", 60)
#Step 3: Print Dog Details and Call Methods

#Print the name and height of each dog.
#Call the bark() and jump() methods for each dog.
print(davids_dog.name)
print(davids_dog.height)
davids_dog.bark()
davids_dog.jump()
print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()
#Step 4: Compare Dog Sizes
#Compare the heights of the two dogs and print which one is taller.
if davids_dog.height > sarahs_dog.height:   
    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")
elif davids_dog.height < sarahs_dog.height:
    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")
else:
    print(f"{davids_dog.name} and {sarahs_dog.name} are the same height.")