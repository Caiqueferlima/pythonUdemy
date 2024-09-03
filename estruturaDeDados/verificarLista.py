cor = input('digite a cor que desejas: ')
cores = ['marrom', 'verde', 'rosa', 'azul']

if cor.lower() in cores:
  print('Disponível')
else:
  print('indisponível')

# o .lower() no if acima serve para transformar o que o cliente digitar em letras minúsculas antes de conferir, assim, evita que seja "Marrom" seja tratado como indisponível, por exemplo 