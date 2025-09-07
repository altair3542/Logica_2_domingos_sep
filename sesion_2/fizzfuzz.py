# Escribe un programa que muestre en pantalla los números del 1 al 100, pero aplicando las siguientes reglas:

# Si el número es múltiplo de 3, muestra la palabra "Fizz" en lugar del número.

# Si el número es múltiplo de 5, muestra la palabra "Fuzz" en lugar del número.

# Si el número es múltiplo de 3 y de 5 al mismo tiempo, muestra "FizzFuzz" en lugar del número.

# Si el número no cumple ninguna condición, muestra el número normalmente.


for numero in range(1, 101):
    if numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Fuzz")
    elif numero % 3 == 0 and numero  % 5 == 0:
        print("FizzFuzz")
    else:
        print(numero)
