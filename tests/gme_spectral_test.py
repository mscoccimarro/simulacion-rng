from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Cambiar valor de la semilla aca
seed = 1
# Cambiar cantidad de iteraciones aca
cantidadIteraciones = 10000

# Devuelve un numero aleatorio utilizando el generador minimo estandar (normalizado)
def generateGME():
  global seed
  a = 16807
  m = (2**31)-1
  seed = (a*seed) % m
  return seed/m

# Genero la secuencia de numeros aleatorios
sequence = []
for i in range(0, cantidadIteraciones):
  sequence.append(generateGME())

# Grafico los numeros de la secuencia en 3 dimensiones 
# siguiendo la logica (x1,x2,x3), (x2,x3,x4), ... para ver como se distribuyen en el espacio
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(0, len(sequence) - 2):
  ax.scatter(sequence[i], sequence[i+1], sequence[i+2], c='b', marker='o')

# Roto el grafico
ax.view_init(30, 60)
plt.show()
