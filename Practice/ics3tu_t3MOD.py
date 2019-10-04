# Here is a program to show how to use "if - elif - else"
# The hash-tag is used to show that these are comments
# This means that the computer will not look at these lines
# Author: Eli Preston
# Upper Canada College

# Put down some options for the user to choose from...
# This progarm is a modification to allow users
# to request useful information from me.


print("What would you like to know?")
print("")
print("1. What is the weather going to be today?")
print("2. What classes do I have today?")
print("3. Do I have an after School Activities")
print(" ")

myrequest = int(input("Choose one. \n")) #newline character "\n"

if myrequest == 1:
    print ("It is going to be sunny today.")
elif myrequest == 2:
    print ("Computer science, English, French, and Gym.")
elif myrequest == 3:
    print ("You have football practice after school today.")
else:
    print ("This is not a valid choice")
    print ("Please input a valid choice.")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")