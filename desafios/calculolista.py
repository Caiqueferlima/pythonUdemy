lista = []

n1 = int(input('digite o primeiro número: '))
n2 = int(input('digite o segundo número: '))

lista.append(n1)
lista.append(n2)

soma = lista[0] + lista[1]
sub = lista[0] - lista[1]
multi = lista[0] * lista[1]
div = lista[0] / lista[1]
exp =lista[0] ** lista[1]

print(f'soma = {soma}, subtração = {sub}, multiplicação = {multi}, divisão = {div}, exponenciação = {exp}')

for i in lista:
  print(f'eu gosto de {i}')