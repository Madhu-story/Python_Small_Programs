# Count the number of letters in the given string:

# str = input("Enter the string: ")
str = "I am learning Python"
letters = len(str)
space = str.count(" ")
num_char = letters - space

print("Count of letters in the given string -->", num_char)