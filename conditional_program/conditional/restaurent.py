# 15. Restaurant Menu

print("1.Pizza  2.Burger  3.Pasta  4.Sandwich  5.Coffee")
choice = int(input("Enter your choice: "))

if choice == 1:
    print("Pizza ₹200")
elif choice == 2:
    print("Burger ₹100")
elif choice == 3:
    print("Pasta ₹150")
elif choice == 4:
    print("Sandwich ₹80")
elif choice == 5:
    print("Coffee ₹50")
else:
    print("Invalid Choice")