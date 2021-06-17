#CONSISTIRÁ EN UNA LISTA Q VA A CONTENER MULTIPLES OPCIONES Y DEBEREMOS ADIVINAR LOS DATOS

dato = input('Ingrese Dato:')

lista = ['hola','mundo','chanchito feliz','drogas duras']

if lista.count(dato) > 0:
    print('El dato existe:', dato)
else: 
    print('El dato: ' + dato + ', No existe :C')
