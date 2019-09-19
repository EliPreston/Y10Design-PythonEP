
import sys



vmRowBreak = 3

vm = [

	{
		"loca": "A1",
		"price": "1.50",
		"item": "Lays Chips"
	},
	{
		"loca": "A2",
		"price": "1.50",
		"item": "Ketchup Chips"
	},
	{
		"loca": "A3",
		"price": "1.50",
		"item": "Ms. Vickeys"
	},
	{
		"loca": "B1",
		"price": "2.50",
		"item": "Mars Bar"
	},
	{
		"loca": "B2",
		"price": "2.50",
		"item": "KitKat"
	},
	{
		"loca": "B3",
		"price": "2.50",
		"item": "Coffee Crisp"
	},
	{
		"loca": "C1",
		"price": "1.50",
		"item": "Perrier"
	},
	{
		"loca": "C2",
		"price": "1.75",
		"item": "Chocolate Milk"
	},
	{
		"loca": "C3",
		"price": "1.00",
		"item": "Water"
	}
]


#-------------------------------------------------------------------------------------------------------------------

welcomeMessage = input("Welcome to the vending machine, please type 'Yes' and then press 'Enter' to continue. \n")



if welcomeMessage == 'no':
	sys.exit()
elif welcomeMessage == 'yes':
	def vmContent():
		count = 0
		print("")
		print("------------------")
		for item in vm:
			if count % vmRowBreak == 0 and count !=0:					#the "%" means if   count/vmRowBreak == to    != means not equal to, == means equal to
				print("------------------")
				count = 0
			print(f"{item['loca']}: {item['item']} -> {item['price']}")
			count += 1				
			# += means "add"

		print("------------------")

vmContent()



#selection = input("Please select a location \n")

#if selection == 'A1' or 'A2' or 'A3':
#	payment = input("Please insert payment \n")
#elif selection !='A1' or 'A2' or 'A3':
#	validity = input("Not a valid input")



while True:
    selection = input("Please choose an item location \n")
    if 'A1' or 'A2' or 'A3' not in selection:
        print("Enter valid selection")
        break
    else:
    	print("insert payment")









