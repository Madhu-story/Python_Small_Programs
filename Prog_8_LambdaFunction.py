# Create a lambda function that takes a number as input and return "Even" if it's even
# and "Odd" if it's odd.

check = lambda number : "Even" if number % 2 == 0 else "Odd"

number = int(input("Enter a number: "))
result = check(number)
print("Given number is:", result)