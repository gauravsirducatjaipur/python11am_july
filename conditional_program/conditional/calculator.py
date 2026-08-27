# # 8. Menu-driven Calculator

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("1.Add 2.Subtract 3.Multiply 4.Divide")

# choice = int(input("Enter choice: "))

# if choice == 1:
#     print("Result =", a+b)
# elif choice == 2:
#     print("Result =", a-b)
# elif choice == 3:
#     print("Result =", a*b)
# elif choice == 4:
#     print("Result =", a/b)
# else:
#     print("Invalid Choice")



print("1.\tAdd\n2.\tSubtract\n3.\tMultiply\n4.\tDivide")
choice = int(input("Enter choice: "))


if choice not in (1,2,3,4):
  print("Invalid Choice")
else:
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))

  if choice == 1:
      print("Result =", a+b)
  elif choice == 2:
      print("Result =", a-b)
  elif choice == 3:
      print("Result =", a*b)
  elif choice == 4:
      print("Result =", a/b)
