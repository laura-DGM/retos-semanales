'''
 Los primeros dispositivos móviles tenían un teclado llamado T9
 con el que se podía escribir texto utilizando únicamente su
 teclado numérico (del 0 al 9).

 Crea una función que transforme las pulsaciones del T9 a su
 representación con letras.
 - Debes buscar cuál era su correspondencia original.
 - Cada bloque de pulsaciones va separado por un guión.
 - Si un bloque tiene más de un número, debe ser siempre el mismo.
 - Ejemplo:
     Entrada: 6-666-88-777-33-3-33-888
     Salida: MOUREDEV
'''

def teclado(entrada):
    salida, valor, dato = [], [], []
    one = [".",",","?","!"]
    two = ["A","B","C"]
    three = ["D","E","F"]
    four = ["G","H","I"]
    five = ["J","K","L"]
    six = ["M","N","O"]
    seven = ["P","Q","R","S"]
    eight  = ["T","U","V"]
    nine = ["W","X","Y","Z"]
    
    for i in entrada+"-":
        #print(i)
        if i == "-":
            salida.append(dato[len(valor)-1])
            valor.clear()
        else:
            valor.append(i)
            if i == "1": 
                dato = one
            elif i == "2": 
                dato = two
            elif i == "3": 
                dato = three
            elif i == "4": 
                dato = four
            elif i == "5": 
                dato = five
            elif i == "6": 
                dato = six
            elif i == "7": 
                dato = seven
            elif i == "8": 
                dato = eight
            elif i == "9": 
                dato = nine
    return print (''.join(salida))

msm = teclado ("6-666-88-777-33-3-33-888-1111")