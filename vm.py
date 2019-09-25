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

def vmContent():
	count = 0
	print("")
	print("------------------")
	for item in vm:
		if count % vmRowBreak == 0 and count !=0:					#the "%" means if   count/vmRowBreak == to    != means not equal to, == means equal to
			print("------------------")
			count = 0

		print(f"{item['loca']}: {item['item']} ....... {item['price']}")
		count += 1				
			# += means "add"
	print("------------------")

vmContent()

selection = input("What item woul you like? Choose a location.\n")

for item in vm: 
	loc = item['loca']
	price = item['price']

	if selection == loc:
		print(price)
		amount = int(input("How many would you like?\n"))
		totalprice = amount*float(price)
		print("Your total for today is $" + str(totalprice))
		theBag = int(input("How much cash you got on you?\n"))

		if float(theBag) >= totalprice:
			change = float(theBag) - totalprice
			print("Your change is $" + str(change))
			print("Thankyou for your purchases")	

		elif float(theBag) < totalprice:
			broke = input("You cannot afford that many items, would you like to buy less items? (y/n)\n")

			if broke == "y":
				amount2 = int(input("How many would you like?\n"))
				totalprice2 = amount2*float(price)
				print("Your revised total is $" + str(totalprice2))
				change2 = int(theBag) - totalprice2
				print("Your change is $" + str(change2))
				print("Thankyou for your purchases.")

			elif broke == "n":
				print("Bye broke boy")
				sys.exit()




