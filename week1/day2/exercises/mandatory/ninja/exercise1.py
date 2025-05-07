#Exercise 1: Cars
car_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
#Convert string to list
cars = car_string.split(",")
print(cars)
#Print out a message saying how many manufacturers/companies are in the list.
print(f"there are {len(cars)} companies in the list")
#Print the list of manufacturers in reverse/descending order (Z-A).
cars.sort(reverse=True)
print(cars)
#Using loops or list comprehension:
#Find out how many manufacturers’ names have the letter o in them.
def count_manufacturers_with_o(cars,letter):
    letter = letter.lower()
    counter_letter = 0
    for car in cars :
     if letter in car :
       counter_letter +=1
    return counter_letter
 
counter_letter_o = count_manufacturers_with_o(cars,'o')
print(counter_letter_o)   

def count_manufacturers_without_i(cars,letter):
      letter = letter.lower() 
      counter_letter = 0
      for car in cars :
        if not letter in car :
         counter_letter +=1
      return counter_letter
#Find out how many manufacturers’ names do not have the letter i in them.
counter_letter_i = count_manufacturers_without_i(cars,'i')
print(counter_letter_i)  
