


day1 = 'Drama, Math, History, Science'
day2 = 'Gym, French, Coding , English'
day3 = 'History, Science, Drama, Math'
day4 = 'English, Coding , French, Gym'
day5 = 'Math, Drama, Science, History'
day6 = 'French, Gym, English, Coding'
day7 = 'Science, History, Math, Drama'
day8 = 'Coding , English, Gym, French'


print("What classes do I have today?")
print("")
print("1")
print("2")
print("3")
print("5")
print("6")
print("7")
print("8")
print("")


whatday = int(input("Which day is it? \n")) #newline character "\n"

today = "Today you have "

if whatday == 1:
    print (today + str(day1))
elif whatday == 2:
    print (today + str(day2))
elif whatday == 3:
    print (today + str(day3))
elif whatday == 4:
    print (today + str(day4))
elif whatday == 5:
    print (today + str(day5))
elif whatday == 6:
    print (today + str(day6))
elif whatday == 7:
    print (today + str(day7))
elif whatday == 8:
    print (today + str(day8))
else:
    print ("This is not a valid choice")
    print ("Please input a valid choice.")


# This is a way to gracefuuly exit the program
input("Press ENTER to quit the program")

