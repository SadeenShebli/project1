mark_1 = int(input("please input your mark\n"))
mark_2 = int(input("please input your mark\n"))
mark_3 = int(input("please input your mark\n"))
if mark_1 < 0 or mark_1 > 100:
    print(" mark_1 is invalid")
elif mark_2 < 0 or mark_1 > 100:
    print(" mark_2 is invalid")
elif mark_3 < 0 or mark_1 > 100:
    print(" mark_3 is invalid")
else:
    avg = (mark_1 + mark_2 + mark_3) / 3.0
    print("your avg is" + str(avg))
    if avg >= 90:
        print("A")
    elif avg >= 80:
        print("B")
    elif avg >= 70:
        print("C")
    elif avg >= 60:
        print("D")
    else:
        print("F")