##Problem 37

##from math import sqrt
##
##def is_prime(n):
##    if n < 2:
##        return False
##    for i in range(2,round(sqrt(n)) + 1):
##        if n % i == 0:
##            return False
##    return True
##
##def is_truncatable_prime(n):
##    nr = n
##    nl = n
##    if len(str(n)) == 1:
##        return False
##    if not is_prime(n):
##        return False
##    right_number = []
##    left_number = []
##    r1 = nl % (int(str(nl)[0]) * 10 **(len(str(nl))-1))
##    left_number.append(r1)
##    while len(str(r1)) != 1:
##        nl = r1
##        r1 = nl % (int(str(nl)[0]) * 10 **(len(str(nl))-1))
##        
##        left_number.append(r1)
##        
##    #left_number.append(n)
##    #print(left_number)
##    r2 = nr // 10
##    right_number.append(r2)
##    while len(str(r2)) != 1:
##        nr = r2
##        r2 = nr // 10
##        right_number.append(r2)
##    #right_number.append(n)
##    #print(right_number)
##
##    for i in left_number:
##        if not is_prime(i):
##            return False
##
##    for j in right_number:
##        if not is_prime(j):
##            return False
##    return True
##    
##s = 0
##for i in range(10,1000000):
##    if not is_truncatable_prime(i):
##        continue
##    print(i)
##    s += i
##print(s)

##Problem 38
############Learn how to concat!!!!!!!!!!!

##def is_pandigital(n):
##    st = str(n)
##    se = set(st)
##    if '0' in se:
##        return False
##    if len(se) == 9:
##        return True
##    return False
##
##def concat(a,b):
##    c = b
##    while(c > 0):
##        a *= 10
##        c //= 10
##    return a + b
##
##             
##
##for n in range(9487,9213,-1):
##    c = concat(n,n*2)
##    if is_pandigital(c):
##        print(c)
##        break


##Problem 39 

##p = 120
##
##max_count = -1
##r = 0
##while p <= 1000:
##    p = p + 1
##    count = 1
##    for a in range(1,p):
##        for b in range(a,p-a+1):
##            for c in range(b,p-a-b+1):
##                if a ** 2 + b ** 2 == c ** 2:
##                    if a + b + c == p:
##                        count += 1
##                        print(a,b,c,p)
##    if count > max_count:
##        max_count = count
##print('**',max_count)

#######according rules, get limitation... faster
##for p in range(2,1001):
##    count = 0
##    for a in range(2, p//3+1):
##        if (p*(p-2*a)) % (2*(p-a)) == 0:
##            count += 1
##    if count > max_count:
##        max_count = count
##        r = p
##print('**',max_count,r)
##        
##    

##Problem 40

##def concat(a,b):
##    c = b
##    while(c > 0):
##        a *= 10
##        c //= 10
##    return a + b
##
##a = [i for i in range(1,1000000)]
##b = []
##for word in a:
##    for i in range(0,len(str(word))):
##        b.append(int(str(word)[i]))
##print(a)
##print(b)
##print(len(b))
##print(b[0],b[9],b[99],b[999],b[9999],b[99999],b[999999])
##print(b[1]*b[10]*b[100]*b[1000]*b[10000]*b[100000]*b[1000000])

##Problem 41

##from math import sqrt
##def is_pandigital(n,s = 9):
##    n = str(n)
##    return len(n) == s and not '1234567890'[:s].strip(n)
##
##def is_prime(n):
##    if n < 2:
##        return False
##    for i in range(2,round(sqrt(n)) + 1):
##        if n % i == 0:
##            return False
##    return True
##
##n = 7654321
##while not(is_pandigital(n,7) and is_prime(n)):
##    n -= 2
##print(n)


##Problem 42
##from math import sqrt
##L = []
##count = 0
##with open('p042_words.txt') as file:
##    for line in file:
##        for word in line.split(','):
##            L.append(word.strip('"'))
##a = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##def word_value(s):
##    result = 0
##    for i in s:
##        result += a.index(i)
##    return result
##
##count = 0
##for i in L:
##    
##    b = word_value(i)
##    if (sqrt(1 + 8 * b) - 1) % 2 == 0:
##        count += 1   
##print(count)

##Problem 43
##########Below brute force is so slow,   got answer by hand...
##def is_pandigital(n, s = 10):
##    n = str(n)
##    return len(n) == s and not '1234567890'[:s].strip(n)
##suma = 0
##for n in range(123456789,987654321):
##    #print(n)
##    s = str(n)
##    if not is_pandigital(n):
##        continue
##    if int(s[3]) % 2 != 0:
##        continue
##    if (int(s[2]) + int(s[3]) + int(s[4])) % 3 != 0:
##        continue
##    if int(s[5]) % 5 != 0:
##        continue
##    if int(s[4:7]) % 7 != 0:
##        continue
##    if int(s[5:8]) % 11 != 0:
##        continue
##    if int(s[6:9]) % 13 != 0:
##        continue
##    if int(s[7:10]) % 17 != 0:
##        continue
##    print(n)
##    suma = suma + n
##
##print(suma)

##Problem 44
##from math import sqrt
##
##for i in range(1,10000):
##    n = i * (3 * i - 1) //2
##    for j in range(i+1,10000):
##        m = j * (3 * j - 1) //2
##        s = n + m
##        d = m - n
####        print(n,m)
####        print((sqrt(24*s+1) +1) % 6 ,(sqrt(24*d+1) +1)% 6)
##        if (sqrt(24*s+1) +1) % 6 == 0 and (sqrt(24*d+1) +1)% 6 == 0:
##            print('%')


##Problem 45
##from math import sqrt
##n = 286
##m = (n*(n+1))//2
##
##while not((sqrt(24*m+1)+1)%6 == 0 and (sqrt(8*m+1)+1)%4 == 0):
##    n = n + 1
##    m = (n*(n+1))//2
##    
##
##print(m)

##Problem 46
from math import sqrt

def is_Glodbach(n):
    if n % 2 == 0:
        return False
    N_index = (n - 1) // 2
    primes_sieve = [True] * (N_index + 1)
    for k in range(1,(round(sqrt(n)) + 1) // 2):
        if primes_sieve[k]:
            for i in range(2 * k * (k + 1), N_index + 1, 2 * k + 1):
                primes_sieve[i] = False
    for i in range(1, N_index + 1):
        if primes_sieve[i]:
            if round(sqrt((n - (2 * i + 1)) // 2)) != sqrt((n - (2 * i + 1)) // 2):
                continue
            return True
    return False
    
n = 35

while is_Glodbach(n):
    n = n + 2
print(n)
    

        
    
        
    
    
