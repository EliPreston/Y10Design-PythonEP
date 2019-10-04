import sys




test = str(input("Write a word.\n"))
with open("fileIO_practice2.txt", "a") as f:
	f.write ("\n" + test)

f.close()






with open("fileIO_practice2.txt", "r") as f:
	for line in f:
		print(line, end = '')



print("")
