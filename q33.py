#write a program to calculate fibonacci sequence at index n fibonacci sequence is  0, 1, 1, 2, 3, 5, 8
# where each number should  equal the previous two numbers


index = 9
a = [0, 1]
i = 2
while i < index:
    a.append(a[i-1]+a[i-2])
    i = i + 1
print(a)



















