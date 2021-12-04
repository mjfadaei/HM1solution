for i in range(2,10000):
    c = 1
    for j in range(2,i):
        if i % j == 0:
            c += j
    if c == i:
        print(c)
print('---------------')      
        
t=0
i=2
while(t != 4):
    sum=0
    for g in range(1,i):
        if(i%g==0):
            sum+=g
    if(sum == i):
        print(i)
        t +=1
        
    i +=1
