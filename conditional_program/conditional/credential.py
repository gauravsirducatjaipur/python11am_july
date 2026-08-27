import random

email = input("Enter your email ")
password = input("Enter your password ")
otp = random.randint(1233,1234)

print("Email is ",email)
print("Password is ",password)
print("otp is ",otp)

if email=="kanak@gmail.com" and password=="1234" and otp==1234:
  print("Login successful")
else:
  print("Login failed")