import numpy as np

# crear un vector
vector=np.array([1,2,3,4])
print(vector)
print(type(vector))
print(id(vector))

#longitud del vector
print(f'longitud usando len {len(vector)}')
print(f'longitud {vector.size}')
print(f'cantidad de dimensiones del vector {vector.shape}') #(3,)Tiene una sola dimensión 

# verificar si es mutable
vector[0]=45
print(vector)
print(type(vector))
print(id(vector))

# agregar elemento y crea un nuevo vector
vector=[1,2,3,4,5]
print(vector)
print(type(vector))
print(id(vector))

# los arrays de numpy tienen un tamaño fijo
vector_nuevo=np.append(vector,25)
print(vector_nuevo)
print(type(vector_nuevo))
print(id(vector_nuevo))

#Matrriz 2D
matriz=np.array([[1,2,3,4,4],[5,4,3,7,4]])
matriz1=np.array([(1,2,3),(3,4,5)])
print(matriz)
print(type(matriz))
print(id(matriz))
#longitud de la matriz 
print(f'longitud usando len {len(matriz)}') #filas
print(f'longitud {matriz.size}') # cantidad de datos
print(f'cantidad de dimensiones del vector {matriz.shape}')# filas * columnas

#operaciones que crean otros arrays
#producto
vector=np.array([1,2,3,4])
print(vector)
print(type(vector))
print(id(vector))

vector1=vector*2
print(vector1)
print(type(vector1))
print(id(vector1))

#concatenado
n_concatenado=np.concatenate([vector,np.array([0,8])])
print(f'concatenado {n_concatenado}, original{vector}')

#Recorrer
for fila in matriz:
    print(fila)

# matriz aleatoria
# matrizaleatoria=np.empty([2,2])
# print(matrizaleatoria)

# matrizaleatoria=np.empty([2,2],dtype=int)
# print(matrizaleatoria)

# vectoraleatorio=np.empty(5)
# print(vectoraleatorio)

# generar matriz zeros

matriceszeros=np.zeros([2,3],dtype=int)
print(matriceszeros)

vectorzunos=np.ones(4)
print(vectorzunos)

# arange
matriz1=np.arange(0,4,2)
print(matriz1)

matriz1=np.arange(0,4).reshape(2,2)
print(matriz1)

matriz1=np.arange(0,4)
print(matriz1)

#sort
a = np.array([89, 34, 56, 87, 90, 23, 45, 12, 65, 78, 9, 34, 12, 11, 2, 65, 78, 82, 28, 78]) 
print(id(a))
print(np.sort(a))
print(id(a))
print(a) #conclusion --> no modifica a a

#ordena in place
a.sort()
print(a)
print(id(a))
#manejo de slicing

arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
print(arr[:]) # muestro toda la matriz
print(arr[:,:]) # muestro toda la matriz
print(arr[1,:]) # fila 1 todas las columnas
print('fila 1 de las columnas 0 a la 3')
print(arr[1,:3]) 
print('muestra filas de la 0 a la 1 en las columnas de la 0 a la 2')
print(arr[:2,:3]) 
print('muestra filas de la 0 a la 1 en las columnas de la 1 y la 3, esto se hace porque el : indica saltar las posiciones')
print(arr[:2,0::2]) 
print('muestra todas filas columna 3')
print(arr[:,3]) 
print('fila 1 solo columna 1 y 3')
print(arr[1,1::2])
print('fila 1 y 3 solo columna 1 y 3')
print(arr[1::2,1::2])
print()