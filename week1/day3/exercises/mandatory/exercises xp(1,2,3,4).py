#Exercise 1 
#Use the provided Cat class to create three cat objects. Then, create a function to find the oldest cat and print its details.
class Cat:
    def __init__(self,name,age):
        self.name = name 
        self.age  = age 
    ## __str__ method to return a string representation of the object
    def __str__(self):
        return f"{self.name}, {self.age} years old"

    
cat1 = Cat("Cat1",2)
cat2 = Cat ("Cat2",3)
cat3 = Cat("Cat3",1)
def find_oldest_cat(cat1, cat2, cat3):
    oldest = cat1
    if cat2.age > oldest.age:
        oldest = cat2
    if cat3.age > oldest.age:
        oldest = cat3
    return oldest
oldest_cat = find_oldest_cat(cat1, cat2, cat3)

# Affichage du résultat formaté
print(f"The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.")

#############################################################################################################################
  
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


#######################################################################################################
#🌟 Exercise 3 : Who’s the song producer?
#Step 1: Create the Song Class

#Create a class called Song.
#In the __init__ method, take lyrics (a list) as a parameter and create a corresponding attribute.
#Create a sing_me_a_song() method that prints each element of the lyrics list on a new line.
class Song:
    def __init__(self,Lyrics):
        self.lyrics = Lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
stairway = Song(["There’s a lady who's sure", "all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()



########################################################################################################################################################
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
    #add 
    def add_animal(self, new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} has been added to {self.name}")
        else:
            print(f"{new_animal} is already in {self.name}")
    
    def get_animals(self):
        print("\nAnimals in", self.name + ":")
        for animal in self.animals:
            print(animal)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold from {self.name}")
        else:
            print(f"{animal_sold} is not in {self.name}")
    
    def sort_animals(self):
        sorted_animals = {}
        for animal in sorted(self.animals):
            first_letter = animal[0]
            if first_letter in sorted_animals:
                if isinstance(sorted_animals[first_letter], list):
                    sorted_animals[first_letter].append(animal)
                else:
                    sorted_animals[first_letter] = [sorted_animals[first_letter], animal]
            else:
                sorted_animals[first_letter] = animal
        return sorted_animals
    
    def get_groups(self):
        sorted_animals = self.sort_animals()
        print("\nAnimal groups in", self.name + ":")
        for letter, animals in sorted_animals.items():
            print(f"{letter}: {animals}")

# instance
new_york_zoo = Zoo("Central Park Zoo")

# Add animals
new_york_zoo.add_animal("Ape")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cat")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Eel")
new_york_zoo.add_animal("Emu")

new_york_zoo.get_animals()
new_york_zoo.sell_animal("Bear")
new_york_zoo.add_animal("Ape")
new_york_zoo.get_groups()



