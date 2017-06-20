# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
x = raw_input("Enter a word to find out if it is a palindrome.")
list = [x]
var2 = int(len(x)/2)
var3 = len(x)
var4 = var3 - var2
for var in range(len(x)):
    list2 = list[var3:] + list[var4] + list[:var2]
    print list, list2, var2, var3, var4
