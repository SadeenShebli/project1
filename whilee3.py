# print 1 -> add students, 2 -> print all students, 3 -> exit
#input -> 3 cases
#if input = 1

students = []
while True:
    print("please input your choice")
    print("1- add students")
    print("2- print student")
    print("3- exit")
    choice = input()
    print(choice)
    if choice == "1":
        std = input("please input new student name\n")
        students.append(std)
    elif choice == "2":
        print(students)
    elif choice == "3":
        print("your index range from 0 to" + str(len(students) - 1))
        index = int(input("please input student index\n"))
        print(students[index])
    elif choice == "4":
        break
    else:
        print("invalid input")
        continue
    print("Thank you")
print("Program end")