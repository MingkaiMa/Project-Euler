##Prpblem_47
##from math import sqrt
##
##def prime_factors(n):
##    L = []
##    i = 2
##    while i * i <= n:
##        if n % i:
##            i += 1
##        else:
##            n //= i
##            L.append(i)
##
##    if n > 1:
##        L.append(n)
##    return L
##
##for i in range(647,100000000):
##    a = set(prime_factors(i))
##    b = set(prime_factors(i + 1))
##    c = set(prime_factors(i + 2))
##    d = set(prime_factors(i + 3))
##
##    if len(a) == 4 and len(b) == 4 and len(c) == 4 and len(d) == 4:
##        print(i)
##        break

##Problem_48
##n = 0
##for i in range(1,1001):
##    
##    n = n + i ** i
##
##print(str(n)[-10:-1] + str(n)[-1])
##


##Problem_49
from math import sqrt
##def is_prime(n):
##    if n == 2:
##        return True
##    if n < 2:
##        return False
##    for i in range(2, round(sqrt(n)) + 1):
##        if n % i == 0:
##            return False
##    return True

##for i in range(1000,10000):
##    if not is_prime(i):
##        continue
##    for j in range(i + 1,10000):
##        if not is_prime(j):
##            continue
##        for k in range(j + 1,10000):
##            if not is_prime(k):
##                continue
##
##            if not (set(str(i)) == set(str(j)) and set(str(j)) == set(str(k))):
##                continue
##            
##                if abs(i - j) != abs(k - j):
##                    continue
##                print(i,j)
##                break
##

##Problem_50               
##def primes(m,n):
##    L = []
##    n_index = (n - 1) // 2
##    primes_sieve = [True] * (n_index + 1)
##    for k in range(1, (round(sqrt(n)) + 1) // 2):
##        if primes_sieve[k]:
##            for i in range(2 * k * (k + 1), n_index + 1, 2 * k + 1):
##                primes_sieve[i] = False
##
##    for j in range(1, n_index + 1):
##        if primes_sieve[j]:
##            if 2 * j + 1 >= m:
##                L.append(2 * j + 1)
##
##    return L
##
##L = primes(1000,10000)
###print(L)
##for i in range(0,len(L)):
##    a = set(str(L[i]))
##    for j in range(i + 1, len(L)):
##        b = set(str(L[j]))
##        if a != b:
##            continue
##        for k in range(j + 1, len(L)):
##            c = set(str(L[k]))
##            if b != c:
##                continue
##            if abs(L[i] - L[j]) != abs(L[k] - L[j]):
##                continue
##            print(L[i],L[j],L[k])
                

##Problem_51
from math import sqrt
def primes(m,n):
    L = []
    n_index = (n - 1) // 2
    primes_sieve = [True] * (n_index + 1)
    for k in range(1, (round(sqrt(n)) + 1) // 2):
        if primes_sieve[k]:
            for i in range(2 * k * (k + 1), n_index + 1, 2 * k + 1):
                primes_sieve[i] = False

    for j in range(1, n_index + 1):
        if primes_sieve[j]:
            if 2 * j + 1 >= m:
                L.append(2 * j + 1)

    return L

L = primes(10000000,99999999)
print(len(L))
            
            





