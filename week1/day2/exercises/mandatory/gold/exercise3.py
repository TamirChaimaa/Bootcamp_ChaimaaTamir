#Exercise 3: Sum
def sum_pattern(X):
    X_str = str(X)
    total = int(X_str) + int(X_str * 2) + int(X_str * 3) + int(X_str * 4)
    return total
# Example:
print(sum_pattern(3))  
