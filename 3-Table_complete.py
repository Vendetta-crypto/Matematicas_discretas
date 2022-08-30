digitHexa = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
             5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
             10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
             15: 'F'}
digit2BaseEleven = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                    10: 'A'}
def decimalToBinario(decimal):
    binario = ""
    while (decimal > 0):
        residuo = decimal % 2
        binario = str(residuo)+ binario
        decimal = int(decimal // 2)
    return binario

def decimalTOctal(decimal):
    octal = ""
    while (decimal > 0):
        residuo = decimal % 8
        octal = str(residuo)+ octal
        decimal = int(decimal // 8)
    return octal

def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        residuo = decimal % 16
        hexadecimal = digitHexa[residuo] + hexadecimal
        decimal = decimal // 16
    return hexadecimal

def decimalToQuintario(decimal):
    quintario = ''
    while(decimal > 0):
        residuo = decimal % 5
        quintario = str(residuo) + quintario
        decimal = decimal // 5
    return quintario

def decimalToSenario(decimal):
    senario = ''
    while(decimal > 0):
        residuo = decimal % 6
        senario = str(residuo) + senario
        decimal = decimal // 6
    return senario
def decimalToBasEleven(decimal):
    eleven = ''
    while(decimal > 0):
        residuo = decimal % 11
        eleven = digit2BaseEleven[residuo] + eleven
        decimal = decimal // 11
    return eleven

for i in range(0,45):
    print(f"Decimal {i}\tBinario {decimalToBinario(i)}\tOctal {decimalTOctal(i)}\tHexadecimal {decimalToHexadecimal(i)}\tQuintario {decimalToQuintario(i)}\tSenario {decimalToSenario(i)}\tBase-11 {decimalToBasEleven(i)}")
