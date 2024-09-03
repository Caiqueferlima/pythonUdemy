def soma(*numbers):
  result = 0
  for num in numbers:
    result += num
  return result


x = soma(4, 5, 6, 7, 8)
print(x)

def agencia(**carro):
  return carro

print(agencia(marca='UNO', cor="vermelho", motor=1.0))