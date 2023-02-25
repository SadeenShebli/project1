#def print_Sadeen(name, age, array):

    #print("Good morning " + name )
    #print(" your age is " + str(age))
   # for a in array:
     #   print(a)

#print_Sadeen("Samia", 20, "hala", "sarah")
#print_Sadeen("Lara", 15, [])
#input 2 redies
#calculate area for each
#compare
def claculate_area(r):
    area = r ** 2 * 3.14
    return area

r1 = int(input("please input r1 \n"))
r2 = int(input("please input r2 \n"))
area1 = claculate_area(r1)
area2 = claculate_area(r2)
if area1 > area2:
    print("area1 is bigger")
elif area2 > area1:
    print("area2 is bigger")
else:
    print("area1 is equal to area2")


