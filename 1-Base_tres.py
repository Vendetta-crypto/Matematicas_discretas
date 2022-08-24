print('='*50)
print("Conversion de numero marciano a cristiano")
print('='*50)
# Obtenemos dato del usuario y lo imprimimos
numero = input('Ingrese un numero en base 3: ')
print(f'usted ingreso:{numero}')
# Separamos el numero desde el punto decimal y los mostramos
y = numero.split('.')
listaInvertida = list(map(int, str(y[0])))
#print(lista2)
#verificamos que no pase el sistema numerico
for d in listaInvertida:
    i = int(d)
    # Verificamos el tipo de dato
    # #print(i,type(i))
    if (0 <= i < 3):
        respuesta = "correcto"
    else:
        respuesta = "incorrecto"

for x in y[1]:
    m = int(x)
    # Verificamos el tipo de dato
    #print(m,type(m))
    if (0 <= m < 3):
        respuesta = "correcto"
    else:
        respuesta = "incorrecto"
#condicion donde si son corrctos los dados se ejecuta el prugrama de lo contrario no se ejecuta la operacion

def invertir_lista(listaInvertida):
    if listaInvertida == []:
        return listaInvertida
    else:
        return [listaInvertida[-1]] + invertir_lista(listaInvertida[:-1])

if (respuesta == "correcto"):
    print(f"La separacion de los numeros a partir del punto es:{y}")
    #inicializamos una variable donde se almacenara la suma de las multiplicaciones
    numero_decimalIZ = 0
    for posicionLi, digito_numIz in enumerate(invertir_lista(listaInvertida)):
        digito = int(digito_numIz)
        multiplicacionIZ = digito * 3**posicionLi
        numero_decimalIZ += int(digito_numIz) * 3**posicionLi
        print(
            f"Digito: {digito_numIz}, Posicion: {posicionLi}, Multiplicacion: {digito_numIz}*3^{posicionLi} = {multiplicacionIZ}")

    numero_decimalD = 0

    for posicionLd, digito_numD in enumerate(y[1], 1):
        digito = int(digito_numD)
        multiplicacionD = digito * 3**-posicionLd
        numero_decimalD += int(digito_numD) * (3**-posicionLd)
        print(
            f"Digito: {digito_numD}, Posicion: {-posicionLd}, Multiplicacion: {digito_numD}*3^{-posicionLd} = {multiplicacionD}")
        resultado = numero_decimalIZ + numero_decimalD

    print(f"El numero decimal es:{resultado}")
else:
    print("ingresa otros datos")

