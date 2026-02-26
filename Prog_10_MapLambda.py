# Write a program to calculate the cube of all numbers in a list: [2, 3, 4]

nums = [2, 3, 4]

cube = list(map(lambda n : n ** 3, nums))
print("Cube of numbers in the list:", cube)