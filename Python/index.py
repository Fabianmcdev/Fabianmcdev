nombre , apellido1 , apellido2 = 'Fabián' , 'Miranda' , 'Catalán'
NombreCompleto = nombre, apellido1,  apellido2
#print (NombreCompleto)
lista = [1,2,3] #se crea lista con sus elementos     #se muestra la lista creada y sus elementos
#lista.pop()     #funcion pop sirve para eliminar el úitimo elemento de la lista

lista.remove(1) #elimina el elemento q se pasa como parámetro en el paréntesis

lista2 = [ 'Tomás','Fabián' ]
print(lista2)

lista2.reverse() #reordena los elementos del final hacia el principio
print(lista2)
lista2.sort()

print(lista2)

#CREACION DE TUPLAS = Son listas NO MODIFICABLES. Si se quieren cambiar, se debe copiar una tupla y agregarle el elemento

FamiliaMirandaChavez = ('Melissa','Fabián','Tomás')

print(FamiliaMirandaChavez[2])

NuevaFamilia = list(FamiliaMirandaChavez)




