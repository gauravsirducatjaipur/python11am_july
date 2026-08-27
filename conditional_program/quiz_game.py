print("Welcome to my game or computer Quiz!")

choice = int(input("Do you want to play\nPress...\n1.\tyes\n2.\tno\n"))
score = 0


if choice==1:
  ans = int(input("What is html?\n1.\thypertext markup language\n2.\tharry markup language\n"))
  if(ans==1):
    score = score+1
  # else:
  #   score = score-1

  ans = int(input("What is CCNA?\n1.\tCisco Certified Network Associate\n2.\tCisco certified Network Academy\n"))
  if(ans==1):
    score = score+1
  # else:
  #   score = score-1
else:
  print("Bye Bye...")



if choice==1:
  print("Your score is",score)

  if(score>0):
    print("You won")
  else:
    print("You loose")
