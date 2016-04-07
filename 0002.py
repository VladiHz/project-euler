def genFibonacci(limite) :
    a = 1
    b = 2
    fib = [a, b]
    while a+b < limite:
        fib.append(a+b)
        a, b = b, a+b
    return fib

def evenList(lista) :
    return filter(lambda x : x%2 ==0, lista)

x = 4000000
# print genFibonacci(x)
print sum(evenList(genFibonacci(x)))
