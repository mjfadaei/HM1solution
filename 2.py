##n = [23,3,45,96,11,7,36,9,27,85]
##for i in range(10):
##    for j in range(i+1,10):
##        if n[i] > n[j]:
##            temp = n[i]
##            n[i] = n[j]
##            n[j] = temp
##print(n)
####
####print("------------------")
####m = [23,3,45,96,11,7,36,9,27,85]
####m.sort()
####print(m)
####
##print("------------------")
##o=[23,3,45,96,11,7,36,9,27,85]
##for i in range(0,len(o)-1):  
##    for j in range(len(o)-1):  
##        if(o[j]>o[j+1]):  
##            temp = o[j]  
##            o[j] = o[j+1]  
##            o[j+1] = temp  
##for i in o:
##    print(i,end="\t")
####
print("------------------")
n = [23 , 3 , 45 , 96 , 11 , 7 , 36 , 9 , 27 , 85]
n = list (n)
n.sort(reverse=True)
print(n)    
##  
