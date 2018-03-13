####Problem 6:

##def sum_of_squares(n):
##    s = 0
##    for i in range(1,n+1):
##        s = s + i*i
##    return s
##
##def squares_of_sum(n):
##    s = 0
##    for i in range(1,n+1):
##        s = s + i
##    return s * s
##print(squares_of_sum(100)-sum_of_squares(100))


####Problem 7:

##from math import sqrt
##
##def prime_list(N):
##
##    N_index = (N - 1) // 2
##    primes_sieve = [True] * (N_index + 1)
##    L = [2]
##    for k in range(1, (round(sqrt(N)) + 1) //2):
##        if primes_sieve[k]:
##            for i in range(2 * k * (k + 1), N_index + 1, 2* k +1):
##                primes_sieve[i] = False
##
##    for n in range(1, N_index + 1):
##        if primes_sieve[n]:
##            L.append(2 * n + 1)
##    print(L[10000])
##    print(len(L))
##
##prime_list(105000)


##Problem 8

##row0 = list('73167176531330624919225119674426574742355349194934')
##row1 = list('96983520312774506326239578318016984801869478851843')
##row2 = list('85861560789112949495459501737958331952853208805511')
##row3 = list('12540698747158523863050715693290963295227443043557')
##row4 = list('66896648950445244523161731856403098711121722383113')
##row5 = list('62229893423380308135336276614282806444486645238749')
##row6 = list('30358907296290491560440772390713810515859307960866')
##row7 = list('70172427121883998797908792274921901699720888093776')
##row8 = list('65727333001053367881220235421809751254540594752243')
##row9 = list('52584907711670556013604839586446706324415722155397')
##row10 = list('53697817977846174064955149290862569321978468622482')
##row11 = list('83972241375657056057490261407972968652414535100474')
##row12 = list('82166370484403199890008895243450658541227588666881')
##row13 = list('16427171479924442928230863465674813919123162824586')
##row14 = list('17866458359124566529476545682848912883142607690042')
##row15 = list('24219022671055626321111109370544217506941658960408')
##row16 = list('07198403850962455444362981230987879927244284909188')
##row17 = list('84580156166097919133875499200524063689912560717606')
##row18 = list('05886116467109405077541002256983155200055935729725')
##row19 = list('71636269561882670428252483600823257530420752963450')
##
##L = [[int(i) for i in row0],[int(i) for i in row1],[int(i) for i in row2],[int(i) for i in row3],[int(i) for i in row4],[int(i) for i in row5]
##     ,[int(i) for i in row6],[int(i) for i in row7],[int(i) for i in row8],[int(i) for i in row9],[int(i) for i in row10],[int(i) for i in row11]
##     ,[int(i) for i in row12],[int(i) for i in row13],[int(i) for i in row14],[int(i) for i in row15],[int(i) for i in row16],[int(i) for i in row17]
##     ,[int(i) for i in row18],[int(i) for i in row19]]
##
##
##M = []
##for i in range(0,20):
##    for j in range(0,50):
##        M.append(L[i][j])
##
##def pro_of_list(lst):
##    p = 1
##    for i in range(0,len(lst)):
##        p = p * lst[i]
##    return p
##
##
##def max_production(n):
##    length = n
##    max_row = 0
##    for i in range(0,1001-length):
##        if 0 in M[i:i+length]:
##            continue
##        if pro_of_list(M[i:i+length]) > max_row:
##            max_row = pro_of_list(M[i:i+length])
##    return max_row
##
##print(max_production(13))

#####Below  understanding wrong....... actually it's easy , see above
##def pro_of_list(lst):
##    p = 1
##    for i in range(0,len(lst)):
##        p = p * lst[i]
##    return p
##
##
##def max_production_row(n):
##    length = n
##    max_row = 0
##    for i in range(0,20):
##        for j in range(0, 51 - length):
##            #print(i,j,j+length)
##            if 0 in L[i][j:j+length]:
##                continue
##            if pro_of_list(L[i][j:j+length]) > max_row:
##                max_row = pro_of_list(L[i][j:j+length])
##    print(max_row)
##    
##max_production_row(13)

##def max_production_column(n):
##    length = n
##    max_column = 0
##    pro = 1
##    for j in range(0,50):
##        for i in range(0, 21 - length):
##            for k in range(i,i+length):
##                if 0 == L[k][j]:
##                    pro = 0
##                    break
##                print(k,j)
##                pro = pro * L[k][j]
##                print(pro)
##            if pro > max_column:
##                max_column = pro
##                print(i,j)
##                print('**',i+length,j)
##                pro = 1
##            pro = 1
##    print(max_column)
##
##max_production_column(13)


##Problem 9

##for i in range(1,500):
##    for j in range(i,500):
##        if i ** 2 + j ** 2 == (1000-i-j) ** 2:
##            print(i*j*(1000-i-j))
##            
##


    


##Problem 10
            
##from math import sqrt
##
##def prime_list(N):
##
##    N_index = (N - 1) // 2
##    primes_sieve = [True] * (N_index + 1)
##    L = [2]
##    for k in range(1, (round(sqrt(N)) + 1) //2):
##        if primes_sieve[k]:
##            for i in range(2 * k * (k + 1), N_index + 1, 2* k +1):
##                primes_sieve[i] = False
##
##    for n in range(1, N_index + 1):
##        if primes_sieve[n]:
##            L.append(2 * n + 1)
##    print(L)
##    print(sum(L))
##
##prime_list(2000000)



##Problem 11

##store the numbers in L
##L = []
##with open('problem_11_file.txt') as file:
##    for i in range(0,20):
##        for line in file:
##            L.append(line.split())
##            
##for i in range(0,20):
##    L[i] = [int(a) for a in L[i]]
##
##def pro_of_list(lst):
##    p = 1
##    for i in range(0,len(lst)):
##        p = p * lst[i]
##    return p
##
##def max_production_row(n):
##    length = n
##    max_row = 0
##    for i in range(0,20):
##        for j in range(0, 21 - length):
##            #print(i,j,j+length)
##            if 0 in L[i][j:j+length]:
##                continue
##            if pro_of_list(L[i][j:j+length]) > max_row:
##                max_row = pro_of_list(L[i][j:j+length])
##    return (max_row)
##    
##def max_production_column(n):
##    length = n
##    max_column = 0
##    pro = 1
##    for j in range(0,20):
##        for i in range(0, 21 - length):
##            for k in range(i,i+length):
##                if 0 == L[k][j]:
##                    pro = 0
##                    break
##                pro = pro * L[k][j]
##            if pro > max_column:
##                max_column = pro
##                pro = 1
##            pro = 1
##    return (max_column)
##
##def max_production_diagonally_right(n):
##    length = n
##    max_dia_right = 0
##    pro = 1
##    for i in range(0,20):
##        for j in range(0,20):
##            m = i
##            n = j
##            while(m < i + length < 20 and n < j + length < 20):
##                if L[m][n] == 0:
##                    pro = 0
##                    break
##                pro = pro * L[m][n]
##                m += 1
##                n += 1
##            if max_dia_right < pro:
##                max_dia_right = pro
##                pro = 1
##            pro = 1
##            
##    return max_dia_right
##
##
##def max_production_diagonally_left(n):
##    length = n
##    max_dia_right = 0
##    pro = 1
##    for i in range(0,20):
##        for j in range(0,20):
##            m = i
##            n = j
##            while(m < i + length < 20 and n >= j +1 - length >= 0):
##                if L[m][n] == 0:
##                    pro = 0
##                    break
##                pro = pro * L[m][n]
##                m += 1
##                n -= 1
##            if max_dia_right < pro:
##                max_dia_right = pro
##                pro = 1
##            pro = 1
##            
##    return max_dia_right
##    
##print(max_production_row(4))
##print(max_production_column(4))
##print(max_production_diagonally_right(4))
##print(max_production_diagonally_left(4)) 


##Problem 12

##from math import sqrt
##
##L = [1]
##for i in range(1,20000):
##    L.append(L[i-1]+i+1)
#####focus below:
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
##        
##for x in L:
##    if nb_of_divisor(x) >= 500:
##        print(x)


##Problem 13

##s = 0
##with open('problem_13_file.txt') as file:
##    for line in file:
##        s = s + int(line)
##print(s)
##print(str(s)[0:10])
 

##Problem 14

##def nb_of_terms(n):
##    count = 1
##    while ( n != 1):
##        if n % 2 == 0:
##            n = n // 2
####            print('*',n)
##            count += 1
##        else:
##            n = 3 * n + 1
####            print(n)
##            count += 1
##    return count
##
####longest_chain = 0
####value = 1
####for i in range(1_000_000,1,-1):
####    if nb_of_terms(i) <= longest_chain:
####        continue
####    longest_chain = nb_of_terms(i)
####    value = i
####
####print(value)
####        

##Problem 15
##C(40,20)

##Problem 16

##p = 2 ** 1000
##
##b = str(p)
##
##L = []
##for i in range(0,len(b)):
##    L.append(int(b[i]))
##
##print(sum(L))
##    







    


    




