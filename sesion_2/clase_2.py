#la variable de control, contador, suma o condicion que regule el ciclo debe estar inicializada.

# x = 5
# while x > 0: # condicion de permanencia
#     print(f'iteracion de x: {x}')
#     x = x - 1 # actualizador de la condicion.
# print('fin')


# errores que generan un bucle infinito:

# No actualizar la condicion dentro del bucle.

# colocar mal la condicion (siempre verdadera o siempre falsa)

# cuando estamos comparando algo usando = en vez de == , esto en python da error, pero hay otros lenguajes donde funciona

# lecturas no acotadas, uso de sentinelas.

# un sentinela es un valor especial que indica 'terminar'

# texto = input("Escribe algo o 'fin' para terminar: ")

# while texto != 'fin':
#     print(f'He leidolo siguiente {texto}')
#     texto = input("Escribe algo o 'fin' para terminar: ")
# print('Listo')


# while true y break

# while True:
#     n = int(input("nummero (0 para terminar: )"))
#     if n == 0:
#         break
#     print(f'cuadrado {n * n}')
# print("terminado")

# sentinela con contadores y acumuladores.

# suma, conteo = 0 , 0

# while True:
#     dato = input("Monto (enter vacio para terminar): ")
#     if dato == "":
#         break
#     monto = float(dato)
#     suma = suma + monto
#     conteo = conteo + 1

# if conteo > 0:
#     print(f'El total es {suma} y el promedio es {suma/conteo}')
# else:
#     print("Joa, no agregate nada mani.")

# Banderas o flags

# una bandera esuna variable booleana que recuerda si paso algo.

# encontrado = False
# while True:
#     palabra = input('Escriba una palabra o X para salir: ')
#     if palabra == "x":
#         break
#     if palabra == 'python':
#         encontrado = True

# if encontrado:
#     print('Aparecio "python" al menos una vez')
# else:
#     print("nunca se escribio la palabra 'python'")


# break y continue.
# Break frena el ciclo
# continue : salta a la siguiente iteracion.

# saltar numeros negaticos y solo vamos a sumar numeros positivos.

suma = 0

while True:
    n = int(input("Número (0 corta): "))
    if n == 0:
        break
    if n < 0:
        print("eso no me sirve, deme otro numero")
        continue
    suma = suma + n
print(f'la suma unicamente de los positivos es {suma}')
