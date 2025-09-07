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
