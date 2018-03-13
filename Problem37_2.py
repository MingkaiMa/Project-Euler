from math import sqrt

n = 1_000_000
prime_list = [2]
N_index = (n - 1) // 2
primes_sieve = [True] * (N_index + 1)

for k in range(1,(round(sqrt(n)) + 1) // 2):
    if primes_sieve[k]:
        for i in range(2 * k * (k + 1), N_index + 1, 2 * k + 1):
            primes_sieve[i] = False

for n in range(1, N_index + 1):
    if primes_sieve[n]:
        prime_list.append(2 * n + 1)

def is_truncatable_prime(n):
    nr = n
    nl = n
    if len(str(n)) == 1:
        return False
    if not n in prime_list:
        return False
    right_number = []
    left_number = []
    r1 = nl % (int(str(nl)[0]) * 10 **(len(str(nl))-1))
    left_number.append(r1)
    while len(str(r1)) != 1:
        nl = r1
        r1 = nl % (int(str(nl)[0]) * 10 **(len(str(nl))-1))
        
        left_number.append(r1)
        
    r2 = nr // 10
    right_number.append(r2)
    while len(str(r2)) != 1:
        nr = r2
        r2 = nr // 10
        right_number.append(r2)


    for i in left_number:
        if not i in prime_list:
            return False

    for j in right_number:
        if not j in prime_list:
            return False
    return True

s = 0
for i in range(10,1000000):
    if not is_truncatable_prime(i):
        continue
    print(i)
    s += i
print(s)


