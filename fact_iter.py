numero = int(input("Digite un numero: " ))

if numero >= 0:
    factorial = 1

    if numero == 0 or numero == 1:
        factorial = 1
    else:
        for i in range(1, numero + 1):
            factorial *= i
    print("factorial : ",factorial)
    #print(f'{numero}! = {factorial}')
else:
    print("El numnero debe ser mayor a 0")