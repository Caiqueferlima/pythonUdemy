#extraindo variáveis de uma lista

frutas = ['goiaba', 'acerola', 'caju', 'manga']

item1, item2, item3, item4 = frutas

produtos = ['caderno', 'lápis', 'fone', 'chaveiro']

item1, item2, item3, *outros = produtos

print(item2)
print(outros)
print(produtos)