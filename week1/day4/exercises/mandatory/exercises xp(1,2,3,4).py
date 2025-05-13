# Exercises 1
# Step 1: Define the base and derived classes

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{self.name} says {sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{self.name} says {sounds}'

# Step 1: Siamese class with a specific attribute
class Siamese(Cat):
    def __init__(self, name, age, eye_color):
        super().__init__(name, age)
        self.eye_color = eye_color  # unique attribute

    def sing(self, sounds):
        return f'{self.name} (with {self.eye_color} eyes) says {sounds}'

# Step 2: Create instances of each cat breed
cat1 = Bengal("Simba", 3)
cat2 = Chartreux("Milo", 5)
cat3 = Siamese("Luna", 2, "blue")

all_cats = [cat1, cat2, cat3]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Walk all the cats
sara_pets.walk()

#######################################################################################################################




#Exercise 2  Dogs
class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        my_strength = self.run_speed() * self.weight
        other_strength = other_dog.run_speed() * other_dog.weight

        if my_strength > other_strength:
            return f"{self.name} wins the fight!"
        elif my_strength < other_strength:
            return f"{other_dog.name} wins the fight!"
        else:
            return "It's a tie!"

dog1 = Dog("Rex", 5, 20)
dog2 = Dog("Buddy", 3, 25)
dog3 = Dog("Rocky", 4, 30)

print(dog1.bark())  
print(dog2.run_speed())  
print(dog1.fight(dog3))  

######################################################################################################################



#🌟 Exercise 3: Dogs Domesticated
from dog import Dog  

import random  

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dog_names):
        names = ", ".join(dog_names)
        print(f"{names} all play together.")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            print(random.choice(tricks))
        else:
            print(f"{self.name} is not trained yet.")

pet_dog = PetDog("Charlie", 4, 22)
pet_dog.train()
pet_dog.play("Rex", "Buddy", "Rocky")
pet_dog.do_a_trick()

############################################################################################################



#Exercise 4
# Step 1: Define the Person class
class Person:
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18

# Step 2: Define the Family class
class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        person = Person(first_name, age)
        person.last_name = self.last_name
        self.members.append(person)

    def check_majority(self, first_name):
        for member in self.members:
            if member.first_name == first_name:
                if member.is_18():
                    print(f"You are over 18, your parents Jane and John accept that you will go out with your friends.")
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member with the first name {first_name} found.")

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        print("Members:")
        for member in self.members:
            print(f"- {member.first_name}, Age: {member.age}")

# Testing the classes
if __name__ == "__main__":
    # Create a family
    my_family = Family("Smith")

    # Add members
    my_family.born("Alice", 20)
    my_family.born("Bob", 16)

    # Check majority
    my_family.check_majority("Alice")  # Should be allowed
    my_family.check_majority("Bob")    # Should not be allowed
    my_family.check_majority("Charlie")  # Not found

    # Present the family
    my_family.family_presentation()
