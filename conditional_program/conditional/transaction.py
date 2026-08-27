cardType = input("Enter the type of the card ").lower()
total_amount = 30000

# DeBiT
# DEBIT

if cardType in ["credit","debit"]:
  cardNumber = input("Enter the card number : ")
  if cardNumber=="12345":
    name = input("Enter your name : ")
    if name=="sumit":
      print("welcome",name)
      cvv=int(input("Enter your cvv : "))
      if cvv==123:
        print("valid cvv next for pin ")
        pin = int(input("Enter your pin number : "))
        if(pin == 8721):
          print("valid pin next for amount")
          amount = int(input("Enter amount which you want to withdraw : "))
          if(amount>total_amount):
            print("Insuffiecient balance, please try again...")
          else:
            total_amount = total_amount - amount
            print("Hello",name,"please collect your amount of",amount,"rupees now balance is",total_amount)
            print("Thanks to visit for using our services, keep it again 🙂")
        else:
          print("Invalid pin number try again")
      else:
        print("Invalid cvv")
    else:
      print("Invalid user")    
  else:
    print("Invalid card number")
else:
  print("Invalid card type")