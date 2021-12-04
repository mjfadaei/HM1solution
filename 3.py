def fibonacci(f) :
    if f == 0:
        return 0
    elif f == 1:
        return 1
    else :
        return fibonacci(f-1) + fibonacci(f-2)
    
print(fibonacci(10))
print('-----------------')

karbar = 10#int(input(" چندمین جمله را می خواهید؟ "))
i = 0
num1 = 0
num2 = 1
if karbar<=0: 
        print("ورودی نادرست وارد کردید") 
elif karbar==1: 
        print(":تا جمله ی", karbar)
else: 
        while  i <karbar :
                # print(num1)
                 q = num1+num2
                 num1=num2
                 num2=q
                 i +=1
print(num1)
print('-----------------')                 

