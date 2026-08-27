import random

start_value = int(input("Enter the starting range of number\t"))
end_value = int(input("Enter the ending range of number\t"))

random_value = random.randint(start_value,end_value)

mychoice = int(input(f"Guess any value between {start_value} to {end_value} \t"))

print("random value is",random_value)
print("my choice is",mychoice)

if(mychoice == random_value):
  print("you won")
else:
  print("you loose")


