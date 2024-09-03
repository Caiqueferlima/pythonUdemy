funcionarios = {'Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa'}
turnoDia = {'Ana', 'Marcos', 'Alice', 'Melissa'}
turnoNoite = {'Pedro', 'Sophia', 'Bruno'}
temCarro = {'Marcos', 'Alice', 'Bruno', 'Melissa'}

print(turnoNoite & temCarro)
print(turnoDia & temCarro)
print(funcionarios - temCarro)