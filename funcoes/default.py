def boasVindas(quantidade, nome='Caíque'):
  print(f'Olá {nome}.')
  print(f'temos {quantidade} laptops')

boasVindas(5)

# a função acima não poderia ser:
# def boasVindas(nome='Caíque', quantidade):
# pois os parâmetros default sempre devem estar no fim
