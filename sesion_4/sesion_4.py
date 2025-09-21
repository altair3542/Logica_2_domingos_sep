# recorrido de listas.
# crear, recorrer, y modificar listas
# cadenas como listas
# patrones clasicos y algoritmos de orden

# que es una lista (areglos, arrays, vectores)
# es un tipo de dato que agrupa a otros tipos de datos con una lectura secuencial, es decir, los datos van ordenados con un indice. este indice va desde 0, que seria la primera posicion. estos se simbolizan o se guardan entre corchete [] y los tipos de datos que almacenan pueden ser todos los primitivos y otros compuestos como tuplas, arreglos y diccionarios.

# edades = [15, 18, 12, 21]
# print(edades)
# print(edades[0])
# edades[3] = 19
# print(edades)
# print(len(edades))

# recorriendo y acumulando valores numericos.

# edades = [12, 15, 18, 21, 19]
# suma = edades[1]
# for i in range(len(edades)):
#     suma = suma + edades[i]
# print(f"promedio: {suma/len(edades)}")

# agregar datos con un input (sabiendo cuantas posiciones vamos a guardar.)

N = 5
datos = []
for _ in range(N):
    x = int(input("Ingrese un numero: "))
    datos.append(x)
    print(datos)
print(f"lista final: {datos}")
print(datos[-1])
