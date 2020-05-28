import sys




test = str(input("Write a word.\n"))
with open("fileIO_practice2.txt", "a") as f:
	f.write ("\n" + test)
f.close()


with open("fileIO_practice2.txt", "r") as f:
	for line in f:
		delete = input("Would you like to delete a line from the list? y/n\n")
		
		if delete == "y":
			line = input("Which line would you like to remove from the list?\n")
			


print("")
