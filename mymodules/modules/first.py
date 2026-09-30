import mymodule

choice = int(input("Enter your choice between 1 to 7 : "))

if choice>=1 and choice<=7:
  num1 = int(input("Enter first number : "))
  num2 = int(input("Enter second number : "))

  if choice==1:
    mymodule.addition(num1,num2)
  elif choice==2:
    mymodule.subtraction(num1,num2)
  elif choice==3:
    mymodule.multiplication(num1,num2)
  elif choice==4:
    mymodule.division(num1,num2)
  elif choice==5:
    mymodule.square(num1)
  elif choice==6:
    mymodule.cube(num1)
  elif choice==7:
    mymodule.power(num1,num2)
else:
  print("You have entered an invalid choice")


