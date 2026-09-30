# f = open('jatin.txt')
# data = f.read()
# print(data)
# f.close()

# with open('jatin.txt') as f:
#   data = f.read()
#   print(data)


# f = open("jatin.txt")
# print(f.readline())
# f.close()


# with open("jatin.txt") as f:
#   print(f.read(5))


# with open("jatin.txt") as f:
#   data = f.readlines()
#   for i in data:
#     print(i)


# with open("jatin.txt") as f:
#   data = f.readlines()
#   print(data)

with open("jatin1.txt", "w") as f:
  f.write("Now the file has some other content!")
  

with open("jatin1.txt", "a") as f:
  f.write("\nHello user")

