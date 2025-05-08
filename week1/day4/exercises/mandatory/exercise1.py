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
