n = [23,3,45,96,11,7,36,9,27,85]
x = maximum = n[0]
for x in range(0,len(n)):
    if n[x] > maximum :
        maximum = n[x]
print("maximum is : ",maximum)

print("--------------------")
print(max(n))

x = maximum = n[0]
for x in n:
    if x > maximum :
        maximum = x
print("maximum is : ",maximum)

print("--------------------")
