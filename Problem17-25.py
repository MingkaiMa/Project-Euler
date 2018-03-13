###Problem 17
##import inflect
##a = inflect.engine()
##L = []
##
##for i in range(1,1001):
##    b = a.number_to_words(i).replace('-','')
##    b = b.replace(' ','')
##    L.append(b)
##
##s = 0
##for i in range(0,len(L)):
##    s = s + len(L[i])
##
##print(s)
    
##def num_to_word(num):
##    ''' words = {} covert an interger number into words]'''
##
##    units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
##    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',\
##             'seventeen', 'eighteen', 'nineteen']
##
##    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', \
##            'eighty','ninety']
##    thousands = ['', 'thousand', 'million', 'billion', 'trillion']
##
##    words = []
##    if num == 0: words.append('zero')
##    else:
##

##Problem 18
##Dynamic Programming

##row0 = list('75'.split())
##row1 = list('95 64'.split())
##row2 = list('17 47 82'.split())
##row3 = list('18 35 87 10'.split())
##row4 = list('20 04 82 47 65'.split())
##row5 = list('19 01 23 75 03 34'.split())
##row6 = list('88 02 77 73 07 63 67'.split())
##row7 = list('99 65 04 28 06 16 70 92'.split())
##row8 = list('41 41 26 56 83 40 80 70 33'.split())
##row9 = list('41 48 72 33 47 32 37 16 94 29'.split())
##row10 = list('53 71 44 65 25 43 91 52 97 51 14'.split())
##row11 = list('70 11 33 28 77 73 17 78 39 68 17 57'.split())
##row12 = list('91 71 52 38 17 14 91 43 58 50 27 29 48'.split())
##row13 = list('63 66 04 68 89 53 67 30 73 16 69 87 40 31'.split())
##row14 = list('04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'.split())
##
##L =[[int(x) for x in row0],[int(x) for x in row1],[int(x) for x in row2],\
##    [int(x) for x in row3],[int(x) for x in row4],[int(x) for x in row5],\
##    [int(x) for x in row6],[int(x) for x in row7],[int(x) for x in row8],\
##    [int(x) for x in row9],[int(x) for x in row10],[int(x) for x in row11],\
##    [int(x) for x in row12],[int(x) for x in row13],[int(x) for x in row14]]
##
##for i in range(13,-1,-1):
##    for j in range(0,i+1):
##        L[i][j] = max(L[i+1][j]+L[i][j],L[i+1][j+1]+L[i][j])
##
##print(L[0][0])


##Problem 19
##from datetime import date
##date_start = date(1901,1,1)
##date_end = date(2000,12,31)
##
##date_start_ord = date_start.toordinal()
##date_end_ord = date_end.toordinal()
##result = 0
##
##for d_ord in range(date_start_ord,date_end_ord+1):
##    d = date.fromordinal(d_ord)
##    if(d.weekday() == 6) and d.day == 1:
##        result += 1
##print(result)

##Problem 20

##def factorial(n):
##    if n == 1 :
##        return 1
##    return n * factorial(n-1)
##s = str(factorial(100))
##L = []
##
##for i in range(0,len(s)):
##    L.append(int(s[i]))
##
##print(sum(L))


##Problem 22

##L = []
##with open('p022_names.txt') as file:
##    for line in file:
##        L = line.split(',')
##        
##
##    
##
####print(L[0])
##L = [x.strip('\"') for x in L]
##R = sorted(L, key = str.upper)
####print(R[0])
####print(R)
##
##a = '_ABCDEFGHIJKLMNOPQRSTUVWXYZ'
##def alphabeticl_value(s):
##    result = 0
##    for i in s:
##        result += a.index(i)
##    return result
##
##result = 0
##for i in range(0,len(R)):
##    
##    result += alphabeticl_value(R[i]) * (i+1)
##
##print(result)


##def nb_of_divisor(n):
##    if n == 1:
##        return 1
##    count = 2
##    for i in range(2, round(sqrt(n)) + 1):
##        if n % i == 0:
##            r = n // i
##            if r == i:
##                count += 1
##            else:
##                count += 2
##    return count

##Problem 23
##from math import sqrt
##
##def is_abundant(n):
##    if n == 0:
##        return False
##    s = 1
##    for i in range(2, round(sqrt(n)) + 1):
##        if n % i == 0:
##            r = n // i
##            if r == i:
##                s = s + i
##            else:
##                s = s + i + r
##    if s > n:
##        return True
##    else:
##        return False
##def not_sum_of_two_abundant(n):
##    for i in range(0,n):
##        if not is_abundant(i):           
##            continue
##        for j in range(0,n):
##            if not is_abundant(j):
##                continue
##            if i + j == n:
##                return False
##            else:continue
##    return True
##L = []
##for i in range(1,28123):
##    if is_abundant(i):
##
##        L.append(i)
##sieve = [True] * 28123
##for i in range(0,len(L)):
##    for j in range(0,len(L)):
##        if L[i] + L[j] <28123:
##            sieve[L[i]+L[j]] = False
##s = 0
##for i in range(1,len(sieve)):
##    if sieve[i]:
##        s = s + i
##print(s)
            

##Problem 24
##import itertools
## a = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9], 10))
## print(a[999999])


##Problem 25

##def fibonacci_v1(n):
##    if n == 1 or n == 2:
##        return 1
##    else:
##        return fibonacci_v1(n-1) + fibonacci_v1(n-2)
##
##from math import sqrt
##def fibonacci_v2(n):
##     return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
##
##
##def fibonacci_v3(n):
##    a = 1
##    b = 0
##    while n > 1:
##        a,b = a+b,a
##        n = n - 1
##    return a
##
##for i in range(100,10000):
##    if len(str(fibonacci_v3(i))) >= 1000:
##        print(i)
##        break


##Problem 26

def length_of_recurring(d):
    length = 1
    a = []
    r = 1 % d

    s = 10 % d
    if s == 0:
        return 0
    u = s
    a.append(s)
    while(s != 1):
 #       print(s)
        s = (s * 10) % d
        
        if u == s:
##            print('*')
            return 1
        else:
            u = s
        if s in a:
            return len(a)-a.index(s)
        else:
            a.append(s)
        if s == 0:
            return 0
        else:
  #          print(s)
            length += 1
    return length

print(length_of_recurring(999))

##for i in range(2,47):
####    print(i)
##    print(length_of_recurring(i), end = ',')
##    
##
##    

max_length = 0
max_value = 0
for i in range(2,1000):
    if length_of_recurring(i) > max_length:
        max_length = length_of_recurring(i)
        max_value = i

print(max_value)
    
