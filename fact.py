def factorialRecu(n):
    if n > 1: #caso base
        return n * factorialRecu(n - 1)
    else:
        return 1

numero = int(input("Digite un numero " ))
print(factorialRecu(numero))