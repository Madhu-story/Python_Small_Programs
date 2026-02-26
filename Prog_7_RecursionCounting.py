# Write a program using recursion to print numbers 1 to 10 without using any loop (for or while):
# HINT: use an 'if' condition to stop the recursion.

i = 1
def calling_num(num):
    global i     
    if i <= num :
        print(i)
        i += 1
        calling_num(num)
               
calling_num(10)