# Write a program using filter() function and lambda expression to extract all the numbers
# which is greater than 50 from a given list. [10, 55 , 32, 75, 90, 41, 68]

nums = [10, 55 , 32, 75, 90, 41, 68]

great = list(filter(lambda n : n > 50, nums))
print(great)