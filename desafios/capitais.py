capitais = [
  {'PAIS': 'Brasil', 'CAPITAL': 'Brasilia'},
  {'PAIS': 'Inglaterra', 'CAPITAL': 'Londres'},
  {'PAIS': 'Alemanha', 'CAPITAL': 'Berlim'}
]

pais = input('digite um país: ')
for i in capitais:
  if pais == i['PAIS']:
    print('Sua capital é', i['CAPITAL'])
    break
  elif pais not in capitais:
    print('país não listado')
    break
