pregunta = input("que operacion quieres hacer? ")
resultado = ()
numero1 = (int(input("ingresa primer numero ")))
numero2 = (int(input("ingresa segundo numero ")))
suma = ("suma")
resta = ("resta")
multiplicacion = ("multiplicacion")
division = ("division")
modulo = ("modulo")
 
 
if pregunta == suma:
    resultado = numero1 + numero2
    print("la suma es ", resultado)
if pregunta == resta:
    resultado = numero1 - numero2
    print("la resta es ", resultado)
if pregunta == multiplicacion:
    resultado = numero1 * numero2
    print("la multiplicacion es ", resultado)
if pregunta == division:
    resultado = numero1 / numero2
    print("la division es ", resultado)
if pregunta == modulo:
    resultado = numero1 % numero2
    print("el modulo es ", resultado)