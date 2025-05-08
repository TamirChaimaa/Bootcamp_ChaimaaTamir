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
