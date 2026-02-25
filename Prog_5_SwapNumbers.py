# Swapping of Variables:

a = 5
b = 6
print("-------Before swapping--------")
print("a: ", a)
print("b: ", b)

# swapping : Method 1
c = a
a = b
b = c
print("-------After swapping- Method 1--------")
print("a: ", a)
print("b: ", b)

# swapping : Method 2 (Using mathematical operators)
a1 = 5
b1 = 6
a1 = a1 + b1
b1 = a1 - b1
a1 = a1 - b1
print("-------After swapping- Method 2--------")
print("a1: ", a1)
print("b1: ", b1)

# swapping : Method 3 (Using mathematical operators)
a2 = 5
b2 = 6
a2 = a2 ^ b2
b2 = a2 ^ b2
a2 = a2 ^ b2
print("-------After swapping- Method 3--------")
print("a2: ", a2)
print("b2: ", b2)

# swapping : Method 4 (Tuple packing and unpacking)
a3 = int(input("Enter 'a3' number: "))
b3 = int(input("Enter 'b3' number: "))
a3, b3 = b3, a3
print("-------After swapping- Method 3--------")
print("a3: ", a3)
print("b3: ", b3)