word = 'PanaJi@12256'

# (a) Total number of alphabets in lowercase
lowercase_count = sum(1 for char in word if char.islower())
print("Total number of alphabets in lowercase:", lowercase_count)  # Output: 4

# (b) Total number of alphabets in uppercase
uppercase_count = sum(1 for char in word if char.isupper())
print("Total number of alphabets in uppercase:", uppercase_count)  # Output: 3

# (c) Total number of numerical in string
numeric_count = sum(1 for char in word if char.isdigit())
print("Total number of numerical in string:", numeric_count)  # Output: 5
