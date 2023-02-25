tup =(20, 60, -15, 2.4, "Sadeen", False)


found = False
for t in tup:
    if t == 2.4:
        found = True
        break
    if t == -15:
        continue
    print(t)
if found == True:
    print("Founded")
else:
    print("not Founded")