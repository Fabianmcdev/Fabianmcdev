
#primerNumero = int(primero)
#segundoNumero = int(segundo)

primero = input('Ingrese primer número: ')

try:
    int(primero)
except:
    primero = 'chanchito'


segundo = input('Ingrese segundo número: ')

try:
    int(segundo)
except:
    segundo = 'chanchito'



if primero == 'chanchito' or segundo == 'chanchito':
    print('Ingresaste mal el dato, ingresa sólo números')
else:
    print(primero + segundo)
