import matplotlib.pyplot as plt

def showHeader(str):
  print('----------------------------------------------')
  print(str)
  print('----------------------------------------------')

def showEnd():
  print('----------------------------------------------')

# Devuelve un array con la secuencia de numeros aleatorios generada (sin normalizar)
# a = multiplicador,
# m = modulo,
# seed = semilla,
# times = cantidad de numeros aleatorios a generar
def lehmerGenerator(a, m, seed, times):
  sequence = [seed]
  for i in range(0, times):
    sequence.append(sequence[i]*a % m)
  return sequence

# Pasa un array de numeros a un formato "imprimible",
# agregando comas entre los numeros y '...' al final
def stringifySequence(numberSequence):
  return ', '.join(str(x) for x in numberSequence) + '...'

sequence = lehmerGenerator(5, 13, 1, 12)

showHeader('Generador de Lehmer: a = 5, m = 13, x1 = 1')
print(stringifySequence(sequence))
showEnd()

# Creo otra iteracion con mayor cantidad de numeros para realizar los graficos
seq1 = lehmerGenerator(5, 13, 1, 23)

# Creo los graficos y los muestro
plt.title('Generador de Lehmer: a = 5, m = 13, x1 = 1')
plt.xlabel('Índice en la secuencia')
plt.ylabel('Número generado')
seqBars = plt.bar(range(1, len(seq1) + 1), seq1)
for bar in seqBars[4:]:
  bar.set_color('green')
plt.show()
