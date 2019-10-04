import sys



f = open("fileIO_practice.txt", "a")
f.write("\n")

sport = str(input("What is your favourite sport.\n"))
hobby = str(input("What is your favourite hobby.\n"))
subject = str(input("What is your favourite subject.\n"))

f.write ("\n" + sport)
f.write ("\n" + hobby)
f.write ("\n" + subject)

f.close()



print("\nPrinting Updated List...")
print("-------------------\n")

f = open("fileIO_practice.txt", "r")
print (f.read())


print("-------------------")
print("\nExiting...")

sys.exit()