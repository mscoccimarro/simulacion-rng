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

sequence = lehmerGenerator(6, 13, 2, 12)

showHeader('Generador de Lehmer: a = 6, m = 13, x1 = 2')
print(stringifySequence(sequence))
showEnd()

# Creo otra iteracion con mayor cantidad de numeros para realizar los graficos
seq1 = lehmerGenerator(6, 13, 2, 23)

# Creo los graficos y los muestro
plt.title('Generador de Lehmer: a = 6, m = 13, x1 = 2')
plt.xlabel('Índice en la secuencia')
plt.ylabel('Número generado')
seqBars = plt.bar(range(1, len(seq1) + 1), seq1)
for bar in seqBars[12:]:
  bar.set_color('green')
plt.show()
