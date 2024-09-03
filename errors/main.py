try:  
  letras = ['a', 'b', 'c', 'd']
  print(letras[4])
except IndexError:
  print('index não existe')

# o else só será executado caso não haja
# erro, ou seja, ele só será executado
# caso o except não seja, e vice-versa.

try:
  valor = float(input('Digite o valor do seu produto: '))
  print(valor)
except ValueError:
  print('digite apenas números')
else:
  print('tudo ok')

# Já o finally, será executado
# independentemente do que vier antes.

try:
  valor = float(input('Digite o valor do seu produto: '))
  print(valor)
except ValueError:
  print('digite apenas números')
finally:
  print('tudo ok')
