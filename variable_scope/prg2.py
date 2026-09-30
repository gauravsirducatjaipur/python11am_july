menus = [
    {
        "name": "Laptop",
        "price": 50000,
        "stock": 10
    },
    {
        "name": "Mobile",
        "price": 25000,
        "stock": 4
    },
    {
        "name": "Tablet",
        "price": 7000,
        "stock": 8
    }
]

while True:

    # Display all items
    print("\n----- Available Items -----")

    for i in range(len(menus)):
        print(
            i + 1,
            menus[i]["name"],
            "Price:", menus[i]["price"],
            "Stock:", menus[i]["stock"]
        )


    # User selects item
    ch = int(input("\nEnter item number to purchase: "))

    # Check valid item number
    if ch < 1 or ch > len(menus):
        print("Invalid item number")
        continue
        # break

    # Select item
    item = menus[ch - 1]

    # Check stock
    if item["stock"] == 0:
        print("Sorry, item is out of stock")
        continue

    # Ask quantity
    qty = int(input("Enter quantity: "))

    # Check quantity with stock
    if qty <= 0:
        print("Please enter a valid quantity")

    elif qty > item["stock"]:
        print("Sorry, only", item["stock"], "items are available")

    else:
        # Deduct stock
        item["stock"] = item["stock"] - qty

        # Calculate total
        total = item["price"] * qty

        print("\n----- Purchase Successful -----")
        print("Item:", item["name"])
        print("Quantity:", qty)
        print("Total Price:", total)
        print("Remaining Stock:", item["stock"])

    # Continue shopping?
    ch = input("\nPress 1 to continue shopping: ")

    if ch != "1":
        break


print("\n----- Final Stock -----")

for item in menus:
    print(
        item["name"],
        "Price:", item["price"],
        "Stock:", item["stock"]
    )

print("\nBye, Thanks for shopping!")

# # # # # import prg1

# # # # # print("The value of x is", prg1.x)

# # # # # x = 8

# # # # # if not x>=10:
# # # # #   print("x is not greater than 10")

# # # # names = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

# # # # for name in names:
# # # #   print(name)


# # # # # for i in range(len(names)):
# # # # #   print(i, names[i])

# # # # # for i in [0,1,2,3,4]:
# # # # #   print(i)

# # # # # for i in range(50):
# # # # #   print(i)

# # # # # i = 0
# # # # # while i<5:
# # # # #   print(i)
# # # # #   i = i+1


# # # x = frozenset({"apple", "banana", "cherry"})
# # # print(x)
# # # print(type(x))
# # # print(id(x))


# # # x = list(x)
# # # print(x)
# # # print(type(x))
# # # print(id(x))


# # def xyz(name="Jatin"):
# #   print(name)




# # xyz()
# # xyz(name="Gaurav")

# menus = [
#   {
#     "name":"Laptop",
#     "price":50000,
#     "stock":10
#   },
#   {
#     "name":"Mobile",
#     "price":25000,
#     "stock":4
#   },
#   {
#     "name":"Tablet",
#     "price":7000,
#     "stock":8
#   }
#   ]

# menus[2]["stock"] = menus[2]["stock"]-3

# print(menus[2]["stock"])

# while True:
#   print("Hello")

#   ch = input("Press 1 to continue\t")
#   if ch == "1":
#     continue
#   break

# print("Bye, Thanks for shopping")