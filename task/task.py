choice = int(input("Enter your choice\nPress 1. Create New List\nPress 2. Edit List\nPress 3. Delete List\nPress 4. View List\nPress 5. Exit\n"))


print("choice is", choice)

def createList():
  global list1
  list1 = []
  listSize = int(input("How many element do u want to add in list "))

  for i in range(listSize):
    element = input("Enter element which u want to add in list ")
    list1.append(element)

  ch = bool(input("do u want to search element in list if yes press anything "))

  if ch=="":
    print("Thank you")
    print(list1)
  else:
    element = input("Enter element which u want to search in list ")
    if element in list1:
      print("Element is present in list")
    else:
      print("Element is not present in list")



if choice == 1:
  createList()
elif choice == 2:
  print("Edit List")
elif choice == 3:
  print("Delete List")
elif choice == 4:
  print("View List")
elif choice == 5:
  print("Exit")
else:
  print("Invalid Choice")