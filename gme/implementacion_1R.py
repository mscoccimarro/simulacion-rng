import math
# Cambiar valor de la semilla aca
seed = 1
# Cambiar cantidad de iteraciones aca
cantidadIteraciones = 10

# Devuelve un número aleatorio entre 0 y 1
def random():
  global seed
  a = 16807.0
  m = 2147483647.0
  temp = a * seed
  seed = temp - (m * math.trunc(temp / m))
  return seed / m

# Imprime valor de la semilla y los numeros aleatorios generados
print("Semilla:", seed)
for i in range(0, cantidadIteraciones):
  print("Iteracion:", i+1, ", Valor:", random())