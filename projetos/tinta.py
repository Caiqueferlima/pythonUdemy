rend = int(input('Rendimento da lata de tinta: '))
h = int(input('Altura da parede: '))
l = int(input('Largura da parede: '))

def calculoTinta():
  m2 = h * l
  print(m2/rend)

calculoTinta()