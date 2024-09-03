reservas = {
301: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 3, "hospede": "Ana Silva"},
302: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 2, "hospede": "Carlos Souza"},
303: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 1, "hospede": "Mariana Lima"},
304: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 5, "hospede": "João Pereira"},
305: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 4, "hospede": "Fernanda Costa"},
306: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 2, "hospede": "Ricardo Alves"},
307: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 1, "hospede": "Patrícia Gomes"},
308: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 3, "hospede": "Lucas Martins"},
309: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 4, "hospede": "Juliana Santos"},
310: {"tipo": "Single", "preco_por_noite": 150.00, "noites_reservadas": 2, "hospede": "Roberto Silva"},
311: {"tipo": "Double", "preco_por_noite": 250.00, "noites_reservadas": 1, "hospede": "Larissa Almeida"},
312: {"tipo": "Suite", "preco_por_noite": 500.00, "noites_reservadas": 3, "hospede": "Eduardo Oliveira"},
}

print('1. Liste todos os quartos do tipo Suite com seus respectivos preços por noite.')
for i in reservas:
    if reservas[i]['tipo'] == 'Suite':
        print(f'O quarto {i}, do tipo {reservas[i]['tipo']}, custa {reservas[i]['preco_por_noite']} por noite')
        
print('')

##############################################################################################################################
print('2. Encontre o quarto com o maior valor total da reserva (preço por noite * número de noites reservadas).')
maiorValor = 0
for i in reservas:
    valor = reservas[i]['preco_por_noite'] * reservas[i]['noites_reservadas']
    if valor > maiorValor:
        maiorValor = valor
        
print('O maior valor total foi de R$', maiorValor)
print('')

##############################################################################################################################
print('3. Calcule o valor total das reservas para cada tipo de quarto.')
suite = double = single = 0

for i in reservas:
    valor = reservas[i]['preco_por_noite'] * reservas[i]['noites_reservadas']
    if reservas[i]['tipo'] == 'Suite':
        suite += valor
    elif reservas[i]['tipo'] == 'Single':
        single += valor
    else:
        double += valor
        
print(f'o valor total gasto com quartos do tipo Suíte foi de R${suite}, do tipo Single foi de R${single} e R${double} do tipo Double.')
print('')

##############################################################################################################################

print('4. Crie um novo dicionário contendo apenas as reservas onde o valor total da reserva (preço por noite * número de noites reservadas) é maior que R$1000, com os respectivos IDs e nomes dos hóspedes.')
reservas2 = {}
for i in reservas:
    valor = reservas[i]['preco_por_noite'] * reservas[i]['noites_reservadas']
    if valor > 1000:
        reservas2 = {i, reservas[i]['hospede']}
        print(reservas2)
        
