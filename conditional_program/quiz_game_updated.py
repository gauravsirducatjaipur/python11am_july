print("Welcome to my game or computer Quiz!")
choice = input("Do you want to play type YES or NO\t")

if choice.lower() == "no":
  print("Okay, maybe next time")
  quit()

score = 0 
print("Okay! Let's play")

answer = int(input("What is HTML?\nPress...\n1.\t\thyper text markup language\n2.\t\thypertext markup language\n3.\t\tharry text markup language\t\t"))

if (answer == 1 or answer== 2):
  print("Correct answer")
  score = score+1
else:
  print("incorrect answer")

answer = int(input("What is CSS?\nPress...\n1.\t\tcascadding stylesheet\n2.\t\tcascadding style sheet\n3.\t\tcascadding styles\t\t"))

if (answer == 1 or answer== 2):
  print("Correct answer")
  score = score+1
else:
  print("incorrect answer")

answer = int(input("What is AI?\nPress...\n1.\t\tartificial intelligence\n2.\t\tartificial intellisence\t\t"))

if (answer == 1):
  print("Correct answer")
  score = score+1
else:
  print("incorrect answer")

wrong_answer = 3-score
print("you have got",score,"right answers and",wrong_answer,"wrong answers")