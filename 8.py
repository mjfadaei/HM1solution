##for i in range(1000,2000+1):
##    flag = True
##    for counter in range(2,i):
##        if (i % counter) == 0:
##            flag = False
##            break
##    if(flag):
##        print(i)
##print("-------------------")
n = 2
m = 1200

NumbersLessThanInput=[x for x in range(n,m )]
PrimeNumbers = []

for x in range(0, len(NumbersLessThanInput)) :
      IsPrimeFlag = 1
      for y in range(0, len(PrimeNumbers)) :
            if NumbersLessThanInput[x] % PrimeNumbers[y] == 0 :
                  IsPrimeFlag = 0
      if IsPrimeFlag == 1:
            PrimeNumbers += [NumbersLessThanInput[x]]
            
print(PrimeNumbers)
print(NumbersLessThanInput)
