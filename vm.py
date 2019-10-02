# Author: Eli Preston
# Upper Canada College



import sys

vmRowBreak = 3
vm = [

	{
		"loca": "A1",
		"price": "1.50",
		"item": "Lays Chips",
		"stock": "10"
	},
	{
		"loca": "A2",
		"price": "1.50",
		"item": "Ketchup Chips",
		"stock": "10"
	},
	{
		"loca": "A3",
		"price": "1.50",
		"item": "Ms. Vickeys",
		"stock": "10"
	},
	{
		"loca": "B1",
		"price": "2.50",
		"item": "Mars Bar",
		"stock": "10"
	},
	{
		"loca": "B2",
		"price": "2.50",
		"item": "KitKat",
		"stock": "10"
	},
	{
		"loca": "B3",
		"price": "2.50",
		"item": "Coffee Crisp",
		"stock": "10"
	},
	{
		"loca": "C1",
		"price": "1.50",
		"item": "Perrier",
		"stock": "10"
	},
	{
		"loca": "C2",
		"price": "1.75",
		"item": "Chocolate Milk",
		"stock": "10"
	},
	{
		"loca": "C3",
		"price": "1.00",
		"item": "Water",
		"stock": "10"
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

		print(f"{item['loca']}: {item['item']} ....... {item['price']} ({item['stock']})")
		count += 1				
			# += means "add"
	print("------------------")

vmContent()


selection = input("All items are in stock. What item would you like? Choose a location.\n")
count = 0
invalidInput = True

for item in vm: 
	loc = item['loca']
	price = item['price']
	stock = item['stock']
	item = item['item']

	if selection == loc:
		print(price)
		amount = int(input("How many would you like?\n"))
		if amount > float(stock):
			print("We do not have that many in stock.")
			sys.exit()

		totalprice = amount*float(price)
		print("Your total for today is $" + str(totalprice))
		print("Please insert payment.")
		theBag = int(input("$"))

		if float(theBag) >= totalprice:
			change = float(theBag) - totalprice
			print("Your change is $" + str(change))
			stockleft = float(stock) - amount
			print("There are " + str(stockleft) + " " + item + " left in stock.")
			print("Thankyou for your purchases")
			break	

		elif float(theBag) < totalprice:
			broke = input("You cannot afford that many items, would you like to buy less items? (y/n)\n")

			if broke == "y":
				amount2 = int(input("How many would you like?\n"))
				totalprice2 = amount2*float(price)
				print("Your revised total is $" + str(totalprice2))
				change2 = int(theBag) - totalprice2
				print("Your change is $" + str(change2))
				print("Thankyou for your purchases.")
				break

			elif broke == "n":
				print("Have a good day random citizen, and come back soon.")
				sys.exit()

	if count == len(vm) - 1:
		print("That is an invald item location.")


	count += 1


