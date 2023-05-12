#!/usr/bin/python3
#numeros enteros#
num_int = 12121
print (num_int)
#numeros negativos#
num_int = -512
print(num_int)
#saber que tipo de datos tenemos#
print (type (num_int))
#float#
num_float = 25.12
print(num_float)
print (type (num_float))
num_float = .9
print(num_float)
num_float = -4.9
print(num_float)
#suma float#
float_test = 1.1 + 2.2
print (float_test)
#simplificar a 2 decomales de resultado#
float_test = 1.1 + 2.2
print(f' {float_test: .2f}')
#char#
country = 'United States'
year_founded = 1776
print(country,year_founded)

color = "blue"
print(color)

notas = [67, 100, 87, 56]
print(notas)

#impresiones#
# 12121
# -512
# <class 'int'>
# 25.12
# <class 'float'>
# 0.9
# -4.9
# 3.3000000000000003
#   3.30
# United States 1776
# blue
# [67, 100, 87, 56]
#impresion con comillas
cadena = "mi libro favorito es 'el principito'"
print(cadena)
# mi libro favorito es 'el principito'
#imprime la posicion
print(cadena[9])
#f
print(cadena[-1])
print(cadena[-6])
print(cadena[-2])
print(cadena[-5])
#rebanada
cadena = "freecodecamp"
print(cadena [2:8])

a = 20
b = 10
print(a + b)

#exponentes
expo = 300000000
print(expo)