# wap to calculate the total cost of items in a shopping cart. suppose i am a shopkeeper and sell three type of item like typeA, typeB and typeC. The price of per item of typeA is 100 rs/ item, typeB is 200 rs/item and typeC is 150 rs/item. Write a program to take input from the user for the quantity of each item and calculate the total cost.

qtyA = int(input("How many item do u want to buy of type A "))
qtyB = int(input("How many item do u want to buy of type B "))
qtyC = int(input("How many item do u want to buy of type C "))

priceA = 100
priceB = 200
priceC = 150

gst_rate = 12

totalAmount = (qtyA * priceA) + (qtyB * priceB) + (qtyC * priceC)

gst_amount = (totalAmount*12)/100
final_amount = totalAmount + gst_amount

print("Total amount is", totalAmount, "after gst final amount is", final_amount)



