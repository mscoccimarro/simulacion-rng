def showHeader(str):
  print('----------------------------------------------')
  print(str)
  print('----------------------------------------------')

def showEnd():
  print('----------------------------------------------')

def lehmerGenerator(a, m, seed, times):
  x = seed
  for i in range(0, times):
    print(x, end="", flush=True)
    print(',', end="", flush=True) if i < times-1 else print('...')
    x = a*x % m


showHeader('Generador de Lehmer: a = 6, m = 13, x1 = 1')
lehmerGenerator(6, 13, 1, 13)

showHeader('Generador de Lehmer: a = 6, m = 13, x1 = 2')
lehmerGenerator(6, 13, 2, 13)
showEnd()