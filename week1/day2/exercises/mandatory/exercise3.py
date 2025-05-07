#🌟 Exercise 3: Zara
#Create a dictionary called brand which value is the information from part one (turn the info into keys and values)
import pprint
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

#Change the number of stores to 2.
brand["number_stores"] = 2
print(brand["number_stores"])


#Print the type of clothes Zara produces.
print(f"{brand['name']} produces clothes for {', '.join(brand['type_of_clothes'])}.")

#Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
print(brand)

#. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand["international_competitors"])

#Delete the information about the date of creation.
del brand["creation_date"]

#Print the last international competitor.
print(f"The last international competitor is {brand['international_competitors'][-1]}.")

# Print the major clothes colors in the US.
print(f"The major clothes colors in the US are {', '.join(brand['major_color']['US'])}.")

#Print the amount of key value pairs (ie. length of the dictionary).
print(f"The brand dictionary has {len(brand)} key-value pairs.")

# Print the keys of the dictionary.
print(f"The keys of the brand dictionary are: {', '.join(brand.keys())}.")

#Create another dictionary called more_on_zara with the following details:
#creation_date: 1975
#number_stores: 10 000
more_on_zara={
    "creation_date": 1975,
    "number_stores": 10000
}

#Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
brand.update(more_on_zara)
#Show the dic on the console using the pprint method.
pprint.pprint(brand)

#Print the value of the key number_stores. What just happened ?
print(f"The number of stores is now {brand['number_stores']}.")
print("What happened is that the key 'number_stores' in the dictionary 'brand' was updated by the .update() method used with the dictionary 'more_on_zara', which contained a new value (10000) for this key.")







