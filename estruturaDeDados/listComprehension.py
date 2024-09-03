frutas1 = ['abacate', 'acerola', 'morango']
frutas2 = []

for items in frutas1:
  if 'r' in items:
    frutas2.append(items)

print(frutas2)

# resumo em 1 linha:

fruit = [items for items in frutas1 if 'r' in items]
print(fruit)