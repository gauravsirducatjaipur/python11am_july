# 11. Transport Fare Calculator

distance = int(input("Enter distance (km): "))

if distance <= 5:
    fare = 50
elif distance <= 15:
    fare = 100
elif distance <= 25:
    fare = 150
else:
    fare = 200

print("Fare =", fare)