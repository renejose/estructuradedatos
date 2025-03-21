print("======================= bienvenidos a mis estructura de datos =========================")

#  estructura de datos :::> almacenar valores 
# str ,bool , int , float
#
# Listas , Tuplas , Conjuntos y Diccionarios 

#variable simple
x = 9 
y = 10 
temp = 0
x = 18

#estructura de datos 
#lista
numeros = [1,2,3,4,5,6,'ReneJose', True, 10 ,11,1,2]
# las listas son mutables
#si permiten valores duplicados

print(numeros)
numeros.append("Ruiz")
print("================== des pues de agregar ===================")
print(numeros)
print(numeros[6])
print("================== despues de meter un valor ===================")
numeros[6] = 19
print(numeros)
numeros.remove(2)
print("================== despues de eliminar ===================")
print(numeros)


#tupla
numeros_primos =(1,2,3,4,5,6,'ReneJose', True, 10 ,11)
# las listas son inmutables
#si permiten valores duplicados

#conjuntos 
numeros_nuevos = {1,2,3,4,5,6,'ReneJose', True, 10 ,11}

#Diccionarios
persona = {
    "nombre" : "Rene jose",
    "edad" : 31,
    "ciudad" : "Piura",
    "correo" : "renejose654@gmail.com"
    }









