# Find the sum of first n natural numbers:

n = int(input("Enter the 'n' natural number to sum up: "))

sum = 0
for i in range(n+1):
    sum += i

print("Sum of", n, "natural number is -->", sum)