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




