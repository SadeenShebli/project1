#input 5 students
# print them
students = []
i = 0
while len(students) < 5:
    std =  input("please input student number" + str(i) +"\n")
    i =  1
    students.append(std)
    if len(students)>=5:
        break

    print(students)