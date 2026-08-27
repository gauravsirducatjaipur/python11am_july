# hindi = input("Enter the marks of hindi subject ")
# english = input("Enter the marks of english subject ")
# maths = input("Enter the marks of maths subject ")
# science = input("Enter the marks of science subject ")
# social = input("Enter the marks of social subject ")

# total = int(hindi) + int(english) + int(maths) + int(science) + int(social)
# percentage = (total/5)
# print("Percentage is ",percentage)

hindi = int(input("Enter the marks of hindi subject "))
english = int(input("Enter the marks of english subject "))
maths = int(input("Enter the marks of maths subject "))
science = int(input("Enter the marks of science subject "))
social = int(input("Enter the marks of social subject "))

total = hindi + english + maths + science + social
percentage = (total/5)

print("Percentage is ",percentage)


if percentage >= 80:
  print("Grade A")
elif percentage >= 60:
  print("Grade B")
elif percentage >= 40:
  print("Grade C")
elif percentage >= 33:
  print("Grade D")
else:
  print("Fail")
