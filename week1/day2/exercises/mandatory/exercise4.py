#🌟 Exercise 4 : Some Geography
#Write a function called describe_city() that accepts the name of a city and its country as parameters.
#Give the country parameter a default value
def  describe_city(city,country="France"):
    #The function should print a simple sentence, such as “city is in country”.
    print(f"{city} is in {country}.")

describe_city("Paris")
