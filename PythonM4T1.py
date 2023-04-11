"""Tipos de datos - cadena de texto (string)"""
mi_cadena = "Hola Mundo!"
print(mi_cadena)
print(type(mi_cadena))

mi_cadena_multilinea = """
Esta es una cadena
de varias lineas
"""
print(mi_cadena_multilinea)
print(type(mi_cadena_multilinea))

"""Tipos de datos - números enteros (integer)"""
entero = 12
print(entero)
print(type(entero))

entero_binario = 0b11
print(entero_binario)
print(type(entero_binario))

entero_octal = 0o12
print(entero_octal)
print(type(entero_octal))

entero_hexadecimal = 0x12
print(entero_hexadecimal)
print(type(entero_hexadecimal))

"""Tipos de datos - números reales (float)"""
real = 7435.28
print(real)
print(type(real))

"""Tipos de datos – números imaginarios/complejos (complex)"""
complejo = 2+3j
print(complejo)
print(type(complejo))

"""Operadores aritméticos"""
#suma
suma = 3 + 2
print(suma)

#resta
resta = 3 - 2
print(resta)

#multiplicación
multiplicacion = 3 * 2
print(multiplicacion)

#division
division = 3 / 2
print(division)

#division entera
division_entera = 3 // 2
print(division_entera)

#módulo
modulo = 3 % 2
print(modulo)

#potencia
potencia = 3 ** 2
print(potencia)

#Un ejemplo sencillo con variables y operadores aritméticos:
monto_bruto = 175
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print("Monto interés: ")
print(monto_interes)
print("Importe bonificación: ")
print(importe_bonificacion)
print("Monto neto: ")
print(monto_neto)

#Prelación de operadores
print(2+3*4)
print((2+3)*4)
print(3*2**2)

"""Operadores lógicos"""
#Y
True and True
True and False
False and True
False and False

#O
True or True
True or False
False or True
False or False

#NO
not True
not False

"""Operadores ralacionales"""
#Mayor
2>1
2>3

#Menor
2<3
2<1

#Mayor o igual
2>=1
2>=2
2>=3

#Menor o igual
3<=2
3<=3
3<=4

#Igual
3==3
3==4

#Diferente
3!=3
3!=4

PI = 3.14159
radio = int(input("Ingrese el radio: "))
print("El área es: " + str(PI * radio ** 2))

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
print("La suma es: " + str(n1 + n2))
print("La resta es: " + str(n1 - n2))
print("La multiplicación es: " + str(n1 * n2))
print("La divsión es: " + str(n1 / n2))

numero = int(input("Ingrese el número: "))
print(str(numero) + " x 1 = " + str(numero * 1))
print(str(numero) + " x 2 = " + str(numero * 2))
print(str(numero) + " x 3 = " + str(numero * 3))
print(str(numero) + " x 4 = " + str(numero * 4))
print(str(numero) + " x 5 = " + str(numero * 5))
print(str(numero) + " x 6 = " + str(numero * 6))
print(str(numero) + " x 7 = " + str(numero * 7))
print(str(numero) + " x 8 = " + str(numero * 8))
print(str(numero) + " x 9 = " + str(numero * 9))
print(str(numero) + " x 10 = " + str(numero * 10))

numero = int(input("Ingrese el número: "))
print((numero >= 3) and (numero < 10))



