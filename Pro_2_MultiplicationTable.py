# Multiplication table for the given number:

t = int(input("Enter a number for the multiplication table: "))
table = 0

for i in range(1, 11):
    table = t * i
    print(t, "*", i, "=", table)