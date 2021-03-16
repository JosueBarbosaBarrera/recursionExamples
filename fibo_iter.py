numerosACalcular = int(input("Digite un numero: "))
num1, num2 = 0, 1
contador = 0

if numerosACalcular <= 0:
    print("El numero debe de ser mayor a 0 ")
elif numerosACalcular == 1:
    print("serie fibonaci de",numerosACalcular,":")
    print(num1)
else:
    print("serie fibonaci :")
    while contador < numerosACalcular:
        print(num1)
        auxiliar = num1 + num2
        num1 = num2
        num2 = auxiliar
        contador += 1