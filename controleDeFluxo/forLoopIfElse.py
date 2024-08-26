compraConfirmada = True
dadosCompra = 'Compra no valor R$12.50 com entrega confirmada'

for enviar in range(3):
  if compraConfirmada:
    print(dadosCompra)
    print('Detalhes enviados para o seu email')
  else:
    print('Falha na compra')
