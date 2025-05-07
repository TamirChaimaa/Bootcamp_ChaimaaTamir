import random

# Step 1: Function to roll a die
def throw_dice():
    return random.randint(1, 6)

# Step 2: Function to roll two dice until a double is obtained
def throw_until_doubles():
    count = 0  # Counts the number of rolls
    while True:
        die1 = throw_dice()
        die2 = throw_dice()
        count += 1
        if die1 == die2:  # If a double is rolled, stop
            break
    return count

# Step 3: Main function
def main():
    throws_list = []  # To store the number of rolls each time
    
    for i in range(100):
        throws = throw_until_doubles()
        throws_list.append(throws)
    
    total_throws = sum(throws_list)
    average_throws = total_throws / len(throws_list)

    print("Total number of rolls to get 100 doubles:", total_throws)
    print("Average number of rolls to get a double:", round(average_throws, 2))

# Call the main function
main()
