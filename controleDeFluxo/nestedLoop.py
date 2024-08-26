for numero1 in range(5):
  print(numero1)
  for numero2 in range(5):
    print(numero2)

# para organizar, pode-se usar o seguinte:
for numero1 in range(1, 6):
  print("Produto " + str(numero1))
  for numero2 in range(1, 6):
    print(str(numero1) + ' ' + str(numero2))