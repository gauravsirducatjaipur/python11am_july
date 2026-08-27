list1 = []

def createList():
    global list1
    list1 = []
    listSize = int(input("How many elements do you want to add in list: "))

    for i in range(listSize):
        element = input("Enter element which you want to add in list: ")
        list1.append(element)

    print("List created successfully")
    print("List is:", list1)

def editList():
    global list1

    if len(list1) == 0:
      print("List is empty so you can't edit it")
    else:
      print("Current List:", list1)

      searchItem = input("Enter element which you want to edit: ")

      if searchItem in list1:
        index = list1.index(searchItem)        
        print(searchItem,"exist on index", index)

        list1[index] = input("Enter new element: ")

        print("List updated successfully")
        print("Updated List:", list1)
      else:
        print("Element is not present in list")
        return


def deleteList():
    global list1

    if len(list1) == 0:
      print("List is already empty")
    else:
      list1.clear()
      # del(list1)
      print("List Item deleted successfully")

def viewList(): 
  if len(list1)==0:
    print("List is empty")
  else:
    for i in range(len(list1)):
      print(str(i+1)+ " element is:", list1[i])

def searchList():
    if len(list1) == 0:
      print("List is empty so you can't search it")
    else:
      element = input("Enter element which you want to search: ")
      if element in list1:
        print("Element is present in list")
        print("Index:", list1.index(element))
      else:
        print("Element is not present in list")



while True:
  choice = int(input("\n\nEnter your choice\n"
        "Press 1. Create New List\n"
        "Press 2. Edit List\n"
        "Press 3. Delete List\n"
        "Press 4. View List\n"
        "Press 5. Search in List\n"
        "Press 6. Exit from List\n"
        ))

  print("Choice is:", choice)


  if choice == 1:
    createList()
  elif choice == 2:
    editList()
  elif choice == 3:
    deleteList()
  elif choice == 4:
    viewList()
  elif choice == 5:
    searchList()
  elif choice == 6:
    print("Thank you")
    break
  else:
    print("Invalid Choice")