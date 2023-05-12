#!/usr/bin/python3
print("alex")
print("alex\'roel")
print("alex 'roel'")

nombre1 = "alex "
nombre2 = "roel"
print(nombre1 + nombre2)


#caracteres de cadenas
nombre = "python"
print(nombre[0])
print(nombre[-1])
print(nombre[5])
print(nombre[-6])
print(nombre[0:2])
print(nombre[:3])
print(nombre[2:])
#si necesito cambiar la 'p' por la 's' debo de hacer este proceso
nombre = "s" + nombre[1:]
print(nombre)
nombre = "ana" + ("pyt" + "o" + nombre[5:])
print(nombre)
#anapyton
nombre = "ana" + ("pyt" + nombre[5:])
print(nombre)
#anapytton
nombre = "ana" + ("pyt" +  nombre[5:])
print(nombre)
#anapyttton
nombre = "ana" + ("pyt"+nombre[5:])
print(nombre)
