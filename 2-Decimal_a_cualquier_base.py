#Hernandez Hernandez Erik Jose
from re import A
import string
digit2Value = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
               5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
                  15: 'F'}

base = int(input("Ingresa la base a convertir: "))
numero = int(input("Ingresa el numero decimal: "))
numero_imprimir = numero
resultado = ""
if base == 16:
    while numero > 0:
        residuo = int(numero % base)
        resultado = digit2Value[residuo] + resultado
        numero = int(numero // base)
    print(f"EL numero {numero_imprimir} es {resultado} en base {base}")
else:
    while numero > 0:
        residuo = int(numero % base)
        resultado = str(residuo) + resultado
        numero = int(numero // base)
    print(f"EL numero {numero_imprimir} es {resultado} en base {base}")



        

