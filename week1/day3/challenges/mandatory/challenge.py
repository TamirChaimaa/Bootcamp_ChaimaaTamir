#Daily challenge: Old MacDonald’s Farm
class Farm:
    def __init__(self, farm_name):
        # ... code to initialize name and animals attributes ...

    def add_animal(self, animal_type, count):
        # ... code to add or update animal count in animals dictionary ...

    def get_info(self):
        # ... code to format animal info from animals dictionary ...


# Test the code 
macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

