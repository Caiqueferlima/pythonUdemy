valores = [10,20,30,45,68]

def remover20(x):
  return x > 20

print(remover20(valores))
print(list(filter(remover20, valores)))