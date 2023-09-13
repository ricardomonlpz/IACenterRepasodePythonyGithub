def isPrime(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    if n <= 3:
        return True  # 2 y 3 son primos

    if n % 2 == 0 or n % 3 == 0:
        return False  # Los múltiplos de 2 y 3 no son primos

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # Si es divisible por algún número entre i e i+2, no es primo
        i += 6  # Los números primos son de la forma 6k ± 1

    return True

# Ejemplos de uso:

for i in range (1,20):
    if isPrime(i+1):
        print(i+1,end=" ")

