print("\n=== Calcuator Program ===\n")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")
print("7. Exit")



choice = int(input("Enter choice (1-7): "))

if choice>=1 and choice<7:
  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))

  if choice == 1:
    print("Result =", num1+num2)
  elif choice == 2:
    print("Result =", num1-num2)
  elif choice == 3:
    print("Result =", num1*num2)
  elif choice == 4:
    print("Result =", num1/num2)
  elif choice == 5:
    print("Result =", num1%num2)
  elif choice == 6:
    print("Result =", num1**num2)
elif choice == 7:
  print("Exit")
else:
  print("Invalid choice")