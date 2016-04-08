import math
def main():
    lista =[2]
    count = 3
    
    while len(lista)<10001:
        isprime = True
        
        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0: 
                isprime = False
                break
        
        if isprime:
            lista.append(count)
        
        count += 1
    print lista
    print min(lista)
    print max(lista)


if __name__ == "__main__":
	main()
# lista = []
# while len(lista) < 10:
# 	x = gen_primes()
# 	print x
# 	lista.append(gen_primes())
# print lista