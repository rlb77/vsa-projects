# Name: Rich
# Date: 6/19/17

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!

User_Name = raw_input("What is your Name?:  ")
firstletter = User_Name[0]
cf = firstletter.upper()
op = User_Name[1:].lower()
print "Your name is", cf + op
User_Age = int(raw_input("How old are you?:  "))
x = ((100-User_Age)+2017)
BD = raw_input("Have you had your birthday this year?:  ")
y = x
if (BD == "no"): y = x - 1
print "You will be 100 in", y
if User_Age < 17: