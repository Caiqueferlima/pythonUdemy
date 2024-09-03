aluno = {'nome': 'Ana', 'idade': 16, 'notaFinal': '9', 'aprovação': True}

print(aluno['aprovação'])

# atualizar key específica
aluno['nome'] = 'Jose'

print(aluno['nome'])

# atualizar diversas keys
aluno.update({'idade': 17, 'notaFinal': 10})
print(aluno)

# adicionar itens
aluno.update({'endereço': 'Rua A'})
print(aluno)
