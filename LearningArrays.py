
"""
people = [

{
	"name": "Eli",
	"age": 15,
	"Last name": "Preston"
},
{
	"name": "Ibrahim",
	"age": 15,
	"Last name": "Fadel"
},
{
	"name": "Will",
	"age": 14,
	"Last name": "Huang"
},
{
	"name": "Marcus",
	"age": "15",
	"Last name": "Renaud"
}

]

# print(person)
# print(person["name"])
# print(person["age"])

# mylist = [person, person2]
print("------------------")

for item in people:
	print(f"Person: {item['name']} {item['Last name']} - {item['age']}")
	print("------------------")

	# print(item)
	# print(f"Person: {item['name']} {item['Last name']} )






"""
#First Attempt At Array For Vending Machine

# print(mylist)

# vm = [
	
# 	'Kitkat'': ''2.00',

# 	'Gatorade'': ''1.75',

# 	'Mars Bar'': ''2.50',

# 	'Gummies'': ''1.50',

# ]

# print("----------------- \n")

# for i in vm:
# 	print(i)
# 	print("----------------- \n")

"""


#-------------------------------------------------------------------
#Ibrahims Example
"""

vmRowSize = 2

vm = [
    {
        "loc": "A1",
        "price": 1.00,
        "item": "chips"
    },
    {
        "loc": "A2",
        "price": 1.00,
        "item": "kitkat"
    },
    {
        "loc": "B1",
        "price": 1.50,
        "item": "mars bar"
    },
    {
        "loc": "B2",
        "price": 2.00,
        "item": "gummies"
    },
    {
        "loc": "C1",
        "price": 3.00,
        "item": "oreos"
    },
    {
        "loc": "C2",
        "price": 2.50,
        "item": "welches"
    }
]

def printContent():
    count = 0
    print("------------------")
    for item in vm:
        if count % vmRowSize == 0 and count != 0:
            print("------------------")
            count = 0
        print(f"{item['loc']}: {item['item']} - {str(item['price'])}")
        count += 1

    print("------------------\n")

printContent()

selection = input("Which item do you want. Select a location(eg. A1)\n\n")








