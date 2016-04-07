# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

n = 600851475143


def isPrime(x):
	if x in primes:
		return True
	else:
		limite = int(math.floor(math.sqrt(x)))
		for prime in primes[1:]:
			if x % prime == 0:
				return False
		for num in range(max(primes)+1,limite+1):
			if x % num == 0:
				return False
		#print primes
		primes.append(x)
		primes.sort()
		return True


limit = int(math.floor(math.sqrt(n)))
print limit
factors=[]
for num in range(2,limit+1):
	if isPrime(num) and n%num==0:
		factors.append(num)
		#break
print max(factors)
# print isPrime(n)
# print primes