####Problem 27
##from math import sqrt
##from time import time
##def is_prime(n):
##    if n <= 0 or n == 1:
##        return False
##    if n == 2:
##        return True
##    for i in range(2, round(sqrt(n))+1):
##        if n % i == 0:
##            return False
##    return True
##
##def function(a,b,n):
##    return (n ** 2 + a * n + b)
##
##
####
####B = []
####for i in range(0,1001):
####    if is_prime(i):
####        B.append(i)
####
####
####current_length = 2
####longest_length = 2
####
####start = time()
####a_final = 0
####b_final = 0
####n = 2
####
#######b must be a prime
#######a is odd:because:
######assume n = 1,  n**2+a*n+b is prime  a+b+1 is prime, b is prime and odd, 1+b is
######even, therefore, a must be odd
####
####for a in range(-1000,1000):
####    if a % 2 == 0:
####        continue
####    for b in B:
#####        current_length = 2
####        n = 2
####        while(is_prime(function(a,b,n))):
####            n += 1
####            current_length += 1
####        if current_length > longest_length:
####            longest_length = current_length
####            a_final = a
####            b_final = b
####            current_length = 2
####        else:
####            current_length = 2
####
####
####print(a_final*b_final)
####print(time()-start)


##Problem 28

##def function(n):
##    b = (n - 1) // 2
##    x = 0
##    y = 0
##    z = 0
##    u = 0
##    for i in range(1,b+1):
##        x += (2 * i + 1) ** 2
##        y += (2 * i + 1) ** 2 - (2 * i)
##        z += (2 * i) ** 2 + 1
##        u += (2 * i) ** 2 - (2 * i - 1)
##
##    return 1 + x + y + z + u
##
##print(function(1001))

##Problem 29

##def distinct_powers():
##    A = []
##    for a in range(2,101):
##        for b in range(2,101):
##            A.append(a ** b)
##    print(len(set(A)))
##distinct_powers()

##Problem 30

##def get_digits(n):
##    r = n % 10
##    L = [r]
##    while(len(str(n)) != 1):
##        n = n // 10
##        r = n % 10
##        L.append(r)
##    return L
##def sum_of_fifth_powers(n):
##    A = get_digits(n)
##    return sum([i ** 5 for i in A])
##
###print(sum_of_fifth_powers(8301))
##
##def sum__of_numbers():
##    result = 0
##    for i in range(2,10000000):
##        if i == sum_of_fifth_powers(i):
####            print(i)
##            result += i
##    print(result)
##
##sum__of_numbers()
##            

##Problem 31
##L = []
##for a in range(0,201):
##    for b in range(0,101):
##        for c in range(0,41):
##            for d in range(0,21):
##                for e in range(0,11):
##                    for f in range(0,5):
##                        for g in range(0,3):
##                            if 0.01 * a + 0.02 * b + 0.05 * c + 0.1 * d + 0.2 * e + 0.5 * f + 1 *g == 2:
##                                print(a,b,c,d,e,f,g)
##                                L.append((a,b,c,d,e,f,g))
##print(len(set(L)))
##from time import time
##L = []
##start = time()
##for g in range(0,3):
##    for f in range(0,(200-100*g)//50+1):
##        for e in range(0,(200-100*g-50*f)//20+1):
##            for d in range(0,(200-100*g-50*f-20*e)//10+1):
##                for c in range(0,(200-100*g-50*f-20*e-10*d)//5+1):
##                    for b in range(0,(200-100*g-50*f-20*e-10*d-5*c)//2+1):
##                        for a in range(0,(200-100*g-50*f-20*e-10*d-5*c-2*b)//1+1):
##                            if a + 2 * b + 5 * c + 10 * d + 20 * e + 50 * f + 100 * g == 200:
## #                               print(a,b,c,d,e,f,g)
##                                L.append((a,b,c,d,e,f,g))
##print(len(set(L)))
##print(time()-start)
##                            


##Problem 32
from time import time
def get_digits(n):
    r = n % 10
    L = [r]
    while(len(str(n)) != 1):
        n = n // 10
        r = n % 10
        L.append(r)
    return L

T = []
start = time()
def pandigital():
    result = 0
    dic = {}
    R = []
    for n in range(1,100):
        for m in range(1,10000):
            if len(str(n))+len(str(m))+len(str(n*m)) != 9:
                continue
            R = get_digits(n)+get_digits(m)+get_digits(n*m)
            if len(set(R)) == 9:
                if 0 in set(R):
                    continue                   
                print(n,m,n*m)
                T.append(n*m)
                result += n * m
                R.clear()
            else:
                R.clear()
    print(result)

pandigital()
print(T)
print(sum(set(T)))
print(time()-start)

##Problem 33

##def get_digits(n):
##    r = n % 10
##    L = [r]
##    while(len(str(n)) != 1):
##        n = n // 10
##        r = n % 10
##        L.append(r)
##    return L
##
##def digit_cancelling_fraction():
##    for n in range(10,100):
##        if 0 in get_digits(n):
##            continue
##        if len(set(get_digits(n))) != 2:
##            continue
##        for m in range(10,100):
##            if 0 in get_digits(m):
##                continue
##            if len(set(get_digits(m))) != 2:
##                continue
##            
##            if len(list(set(get_digits(n))-set(get_digits(m)))) == 0 or len(list(set(get_digits(n))-set(get_digits(m)))) == 2:
##                continue
##            if len(list(set(get_digits(n))-set(get_digits(m)))) == 0 or len(list(set(get_digits(n))-set(get_digits(m)))) == 2:
##                continue
##            a = list(set(get_digits(n))-set(get_digits(m)))[0]
##            b = list(set(get_digits(m))-set(get_digits(n)))[0]
##            if a * m == n * b:
##                print(n,m,a,b)
##            
##digit_cancelling_fraction()           

##Problem 34

##from time import time
##start = time()
##def factorial(n):
##    if n == 0 or n == 1:
##        return 1
##    return n * factorial(n-1)
##
##def get_digits(n):
##    r = n % 10
##    L = [r]
##    while(len(str(n)) != 1):
##        n = n // 10
##        r = n % 10
##        L.append(r)
##    return L
##
##def digit_factorial():
##    sumall = 0
##    for n in range(3,100000):
##        R = get_digits(n)
##        if factorial(max(R)) >= n:
##            continue
##        if sum([factorial(i) for i in R]) == n:
##            print(n)
##            sumall += n
##    print(sumall)
##digit_factorial()

##Problem 35
##from math import sqrt
##def reverse_number(n):
##    if len(str(n)) == 1:
##        return n
##    return int(str(n)[::-1])
##
####print(reverse_number(3))
##
##def is_prime(n):
##    if n < 2:
##        return False
##    for i in range(2,round(sqrt(n)) + 1):
##        if n % i == 0:
##            return False
##    return True
##
##def get_digits(n):
##    r = n % 10
##    L = [r]
##    while(len(str(n)) != 1):
##        n = n // 10
##        r = n % 10
##        L.append(r)
##    return L
##
##from collections import deque
##
##
##
##def is_circular_prime(n):
##    if not is_prime(n):
##        return False
##    N = n
##    a = deque()
##    if len(str(n)) == 1:
##        return True
##    if len(str(n)) == 2:
##        if is_prime(n) and is_prime(reverse_number(n)):
##            return True
##        else:
##            return False
##    r = n % 10
##    a.append(r)
##    while(len(str(n)) != 1):
##        n = n // 10
##        r = n % 10
##        a.appendleft(r)
##    for i in range(0,len(str(N))-1):
##        a.rotate()
##        if not is_prime(int(''.join(str(j) for j in a))):
##            return False
##    return True
##        
##
##
##from time import time
##start = time()
##def circular_primes(n):
##    s = 0
##
##    for i in range(2,n+1):
##        if is_circular_prime(i):
##            print(i)
##            s = s + 1
##    print(s)
##
##circular_primes(1000000)
##print(time()-start)

##Problem 36
##from time import time
##start = time()
##def palindromes():
##    suma = 0
##    for n in range(0,1000000):
##        a = str(n)
##        b = bin(n)[2:]
##        if a[0] == 0:
##            continue
##        if b[0] == 0:
##            continue
##        if a == a[::-1] and b == b[::-1]:
##            suma += n
##    return suma
##print('*',palindromes())
##print(time()-start)
##        






        
