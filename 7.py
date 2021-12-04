n = 11
flag = "yes"
for i in range(2,n):
    print(i)
    print("+")
    if (n % i) == 0:
        flag = "no"
        break
print("is 10 prime?",flag)

print('------------------')
##number = int(input('please input your number: '))
##summ = 0
##for i in range(1, number+1):
##    if number%i == 0:
##        summ+=1
##if summ==2:
##    print('Yes!')
##else:
##    print('No!')
##    
##print('------------------')
##num = 23543
##if num > 1:
##    for i in range(2, int(num/2)+1):
## 
##        if (num % i) == 0:
##            print("yes")
##            break
##    else:
##        print(num, "no")
##print('------------------')        
##x = 23543

##if x > 1 and x != 4:
##    for i in range(2 , x//2):
##        if x % i == 0:
##            print('No')
##            break
##    else:
##        print('yes')  
##
##else:
##    print('No')
