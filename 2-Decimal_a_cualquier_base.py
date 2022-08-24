import string

base = int(input("Ingresa la base a convertir: "))
numero = int(input("Ingresa el numero decimal: "))
resultado = ""
while numero  > 0:
    residuo = int(numero % base) 
    numero = int(numero  / base)
    resultado = str(residuo) + resultado
    
print(f"EL numero {numero} es {resultado} en base {base}")

        

