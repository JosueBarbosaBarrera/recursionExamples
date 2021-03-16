numerosACalcular = int(input("Digita un numero: "))
def fibo(n):
    if n <= 1:
        return n
    else:
        return (fibo(n-1) + fibo(n-2))

if numerosACalcular <= 0:
    print("Debe ser mayor a 0")
else:
    print("secuencia fibonaci: ") #imprime seriede numeros en secuencia fibonaci
    for i in range(numerosACalcular):
        print(fibo(i))