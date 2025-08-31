#Que es un bucle?

#Estructura de control (ejecuta codigo de forma secuencial y controlada, segun el conjunto de instrucciones o condiciones que apliquemos.) de forma repetitiva.

# Secuencialidad: instrucciones que se ejecutan una tras otra.

# Condicional: ejecuta codigo segun una decision tomada, dada una condicion. (if, elif, else)

# Repetitivas: repetir un bloque de codigo mientras se cunpla uina condicion o durante un rango definido. se usa cuando: se debe repetir la misma operacion varias veces o no conocemos de antemano cuantas veces vamos a repetir una accion o si lo sabemos...

#Panorama de los bucles...

# PARA (for): repite un numero conocido de veces o recorre una secuencia o rango.

# MIENTRAS (while): repite el codigo mientras la condicion sea verdadera (riesgo de que el bucle sea infinito si no se cambia la variable que lo rige.)

# REPETIR…HASTA / do-while: ejecuta al menos una vez y luego verifica la condición.

# El bucle For.
# recorriendo un rango simple

# for i in range(incial, fin, paso):
    # codigo que se va a ejecutar, usando i como variable iteradora.

# range(n) = contar desde 0 hasta n-1
# range(100) = 0 ... 99
# range(a, b) = a hasta b - 1
# range(350, 499) = 350 ... 498
# range(a, b, s) = a, a+s, a+2s, a+3s .... b (paso puede ser negativo)
# range(1, 1001, 10) = 1, 10, 20, 30, ... 1000
# range(1000 - 0, -10) = 1000, 990, 980, 970 ... -1

# 1= imprimir numeros del 0 al 4

# for i in range(5):
#     print(i)

# # 2) imprimir los numeros del 1 al 5
# print('segundo ejercicio')

# for i in range(1, 6):
#     print(i)

# # 3) imprimir los numeros pares del 0 al 20
# print('tercer ejercicio')

# for i in range(0, 21, 2):
#     print(i)

# # 4) imprimir los numeros del 1 al 20, de forma descendente
# print('cuarto ejercicio')

# for i in range(20, -100,-1):
#     print(i)
