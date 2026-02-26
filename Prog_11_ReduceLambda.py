# Write a program to calculate the sum of the cube of all numbers in a list: [2, 3, 4]

from functools import reduce

nums = [2, 3, 4]

cube = list(map(lambda n : n ** 3, nums))
sum = reduce(lambda a, b : a + b, cube)
print("Cube of numbers in the list:", cube)
print("Sum of numbers:", sum)