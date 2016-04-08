# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
#       47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n = 600851475143
factors = []


def pfactors(num):
    global factors
    limit = int(math.floor(math.sqrt(num)))
    for i in xrange(2, limit+1):
        dm = divmod(num, i)
        if dm[1] != 0:
            continue
        else:
            factors.append(i)
            num = dm[0]
            #pfactors(dm[0])
    #factors.sort()
    return factors

    # break
#print max(factors)
print pfactors(n)
# print primes
