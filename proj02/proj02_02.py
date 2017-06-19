# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13...
"""
pre = 1
new = 1
x = int(raw_input("How many Fibonacci numbers do you want to find?"))
for var in range(x):
    var = pre + new
    pre = new
    new = var
    print pre