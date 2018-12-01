import matplotlib.pyplot as plt

def showHeader(str):
  print('----------------------------------------------')
  print(str)
  print('----------------------------------------------')

def showEnd():
  print('----------------------------------------------')

def lehmerGenerator(a, m, seed, times):
  sequence = [seed]
  for i in range(0, times):
    sequence.append(sequence[i]*a % m)
  return sequence

def stringifySequence(numberSequence):
  return ', '.join(str(x) for x in numberSequence) + '...'

sequence1 = lehmerGenerator(6, 13, 1, 13)
sequence2 = lehmerGenerator(6, 13, 2, 13)

showHeader('Generador de Lehmer: a = 6, m = 13, x1 = 1')
print(stringifySequence(sequence1))

showHeader('Generador de Lehmer: a = 6, m = 13, x1 = 2')
print(stringifySequence(sequence2))
showEnd()

seq1 = lehmerGenerator(6, 13, 1, 20)
seq2 = lehmerGenerator(6, 13, 2, 20)

plt.title('Generador de Lehmer: a = 6, m = 13, x1 = 1')
plt.xlabel('Índice en la secuencia')
plt.ylabel('Número generado')
seqBars = plt.bar(range(1, len(seq1) + 1), seq1)
for bar in seqBars[12:]:
  bar.set_color('green')
plt.show()

plt.title('Generador de Lehmer: a = 6, m = 13, x1 = 2')
plt.xlabel('Índice en la secuencia')
plt.ylabel('Número generado')
seqBars = plt.bar(range(1, len(seq2) + 1), seq2)
for bar in seqBars[12:]:
  bar.set_color('green')
plt.show()