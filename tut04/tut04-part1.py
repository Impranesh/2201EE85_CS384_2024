def add_student():
  student={}
  while True:
    name=input("Enter student name or 'done' to exist:")
    if(name=="done"):
      break
    else:
      student.update({name:[]})
      grades=[]
      while True:
                grade=int(input("Enter student grade or -1 to exist:"))
                if(grade==-1):
                  break
                grades.append(grade)
      student[name]=grades

  return student
def update_student(students_data,student,index):
  if(len(students_data[student])!=0 ):
    students_data[student][index]=int(input("Enter new grade:"))
  else:
    print("Student not found")
    new_student_name = input("If you want to add then enter new Student name again else done:")
    if(new_student_name!="done"):
      student_data=add_student()
  return students_data
def delete_student(students_data,student):
  if(len(students_data[student])!=0):
    del students_data[student]
  else:
    print("Student not found")
  return students_data
def average(students_data,student):
  if(len(students_data[student])==0):
    print("Student not found")
    return
  else:
    sum=0
    for i in students_data[student]:
      sum+=i
    return sum/len(students_data[student])

def sort_students_by_average(students_data):
  averages = {}
  for student, grades in students_data.items():
    if grades:
      averages[student] = sum(grades) / len(grades)

  student_list = list(averages.keys())
  for i in range(len(student_list)):
    for j in range(i + 1, len(student_list)):
      if averages[student_list[i]] < averages[student_list[j]]:
        student_list[i], student_list[j] = student_list[j], student_list[i]

  return student_list




while True:
    a=input("Enter the Operations On Student database You Want: add,update,average,sort and none to exits.")
    if(a=="none"):
      break
    else:
      if(a=="add"):
        students_data=add_student()
      elif(a=="update"):
        student=input("Enter student name:")
        for i in range(len(students_data[student])):
          print(i,students_data[student][i])
        index=int(input("Enter index of grade:"))
        students_data=update_student(students_data,student,index)
      elif(a=="delete"):
        students_data=delete_student(students_data,student)
      elif(a=="average"):
        student=input("Enter student name:")
        print(average(students_data,student))
      elif(a=="sort"):
        print(sort_students_by_average(students_data))

      else:
            print("Invalid")

    print(students_data)