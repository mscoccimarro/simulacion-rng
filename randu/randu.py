from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

# Cambiar valor de la semilla aca
seed = 1
# Cambiar cantidad de iteraciones aca
cantidadIteraciones = 10000

# Devuelve un numero aleatorio utilizando el generador RANDU (normalizado)
def generateRANDU():
  global seed
  a = 65539
  m = 2**31
  seed = (a*seed) % m
  return seed/m

# Genero la secuencia de numeros aleatorios
sequence = []
for i in range(0, cantidadIteraciones):
  sequence.append(generateRANDU())

# Creo puntos en 3 dimensiones siguiendo la logica (x1,x2,x3), (x2,x3,x4), ...
# seqPoints = []
# for i in range(0, len(sequence) - 2):
#   seqPoints.append([sequence[i], sequence[i+1], sequence[i+2]])

# Grafico los puntos de 3 dimensiones para ver como se distribuyen en el espacio
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# for i in range(0, len(seqPoints)):
#   ax.scatter(seqPoints[i][0], seqPoints[i][1], seqPoints[i][2], c='b', marker='o')

for i in range(0, len(sequence) - 2):
  ax.scatter(sequence[i], sequence[i+1], sequence[i+2], c='b', marker='o')

# Roto el grafico para que se pueda ver que se forman 15 hiperplanos paralelos
ax.view_init(30, 60)
plt.show()
