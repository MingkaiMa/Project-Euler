##Problem 1
##result=0
##for i in range(1,1000):
##    if i % 3 == 0 or i % 5 == 0:
##
##        result += i
##print(result)

##Problem 2
##def fibonacci(n):
##    if n == 0 or n ==1:
##        return n
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##
##L = [0,1,2]
##
##for i in range(1,31):
##        
##        L.append(L[i]+L[i+1])
##
##print(L)
##
##result=0
##for i in L:
##    if i % 2 ==0:
##        result += i
##print(result)



##Problem 3

##def is_prime(n):
##    if n == 1:
##        return False
##    if n == 2 :
##        return True
##    for i in range(2,int(n**(0.5))+1):
##
##        if n % i ==0:
##            
##            return False
##    return True
##
##n = int(input('Input...'))
##
##def largest_prime_factor(n):
##    if is_prime(n):
##        return n

##online method,
##    while n > 1:
##        for i in range(2,n+1):
##            if n == i:
##                return n
##            if n % i == 0:
##                n = n // i
##                break

##    
##        
##    

##My own metohd
##    while n > 1:
##        for i in range(1,n//2 + 1):
##            if not is_prime(i):
##                continue
##            if n%i != 0:
##                continue
##            if is_prime(n//i):
##                return (n//i)
##            else:
##                n = n//i
##                break
## 
##           
            
##
##result = largest_prime_factor(n)
##print(result)
##

##online method not correct 100%
##n = 6
##i = 2
##
##while i * i < n:
##    while n % i == 0:
###        print(n,i)
##        n = n//i
##
##    i += 1
##
## #   print('*',i)
##
##print('**',n)
##        
        
##Problem 4

##
##def is_palindromic(s):
##    if str(s) == str(s)[::-1]:
##        return True
##    return False
##
##def largest_palindromic_number():
##    max_number = 0
##    for i in range(999,99,-1):
##        for j in range(999,99,-1):
##            if str(i*j) == str(i*j)[::-1]:
##                if max_number < i*j:
##                    max_number = i*j
##    print(max_number)
##               
##                
##            
##
##largest_palindromic_number()
##print(largest_palindromic_number())


##Problem 5:
from functools import reduce
def gcd(a,b):
    r = a % b
    if r:
        return gcd(b,r)
    else:
        return b

def lcm(a,b):
    return a*b // gcd(a,b)

def lcmAll(seq):
    return reduce(lcm,seq)
lst = [a for a in range(1,21)]
print(lcmAll(lst))


            
    

##Problem 21:

##from math import sqrt
##
##def sum_of_divisor(n):
##    s = 0
##    for i in range(1,n//2 + 1):
##        if n % i == 0:
##            s += i
##    return s
##answer=0
##for x in range(4,10000):
##    if sum_of_divisor(x) > 4:
##        if sum_of_divisor(sum_of_divisor(x)) == x and sum_of_divisor(x) != x:
##            answer += x
##
##print(answer)

            
        
    
    
