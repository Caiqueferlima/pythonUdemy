aluno = {
  'nome': 'Ana',
  'idade': 16,
  'nota': 7.5,
  'materias': ['Física', 'Inglês', 'Geografia']
}

for x in aluno.values():
  print(x)

for x in aluno.items():
  print(x)

for keys, values in aluno.items():
  print(keys, values)

