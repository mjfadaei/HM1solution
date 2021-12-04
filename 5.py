##greatest common divisor
n = 654
m = 744

def bmm(m , n):
    if m%n ==0 :
        return n
    else:
        return bmm(n , m%n)
print(bmm(m , n))
print('----------------------')

def gcd(m, n):
 if (m == 0):
  return n
 if (n == 0):
  return m

 if (m == n):
  return m

 if (m > n):
  return gcd(m - n, n)
 return gcd(m, n - m)


m = 654
n = 744
if (gcd(m, n)):
 print('GCD of', m, 'and', n, 'is', gcd(m, n))
else:
 print('not found')
print('----------------------')
def gcd2(m, n):
    for i in range(1,min(m,n)+1):
        print(i)
        if m%i == 0 and n%i == 0:
            temp = i
    return temp


m = 6
n = 12
print('GCD of', m, 'and', n, 'is', gcd2(m, n))


 
