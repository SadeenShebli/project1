#write a program to calculate summation of the numbers from n to m for example the summation of when n=3 and m=9 is  3+4+5+6+....9 = 42 ?
#Note: n should be always less than m
n = int(input())
m = int(input())
sum = 0
for i in range(n, m + 1):
        sum =  sum + i
        print(sum)








