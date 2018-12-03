# Cambiar valor de la semilla aca
seed = 1
# Cambiar cantidad de iteraciones aca
cantidadIteraciones = 10

# Devuelve un número aleatorio entre 0 y 1
def random():
  global seed
  a = 16807
  m = 2147483647
  q = 127773
  r = 2836
  hi = seed // q
  lo = seed % q
  test = a*lo - r*hi
  if (test > 0):
    seed = test
  else:
    seed = test + m
  return seed / m

# Imprime valor de la semilla y los numeros aleatorios generados
print("Semilla:", seed)
for i in range(0, cantidadIteraciones):
  print("Iteracion:", i+1, ", Valor:", random())