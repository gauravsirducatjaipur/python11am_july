NUM_OF_STUDENTS = int(input('Enter the number of students:'))

stuData = []

for i in range(NUM_OF_STUDENTS):
  print('\nEnter the data of student', i+1)
  name = input('Enter the name ')
  rollno = int(input('Enter the roll no '))
  marks = int(input('Enter marks '))


  if marks > 95:
    grades = 'A+'
  elif marks> 80:
    grades = 'A'
  elif marks > 65:
    grades = 'B'
  elif marks > 50:
    grades = 'C'
  else:
    grades = 'd'



  students = {'name' : name, 'rollno' : rollno, 'marks' : marks,'grades' : grades}

  stuData.append(students)



# print(stuData)


        
#DATA PRINTING SECTION 


print('\n The data of all students are: ')

for s in stuData:
    print(f"{s['name']} - Rollno : {s['rollno']} - Marks :  {s['marks']} - Grades :  {s['grades']} ")


# for item in stuData:
#   print("name is", item['name'])
#   print("rollno is", item['rollno'])
#   print("marks is", item['marks'])
#   print("grades is", item['grades'])


# # PASS STUDENTS DATA SECTION 

print('\n students who are passed')

for s in stuData:
    if s['marks'] >= 33:
        print(f" {s['name']} - Marks {s['marks']} ")