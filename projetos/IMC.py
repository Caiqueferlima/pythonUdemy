h = float(input('Qual sua altura? '))
kg = float(input('Qual seu peso em kg? '))
h *= h
imc = kg/h
if(imc < 18.5):
  print('magreza')
elif(imc >= 18.5 and imc < 25):
  print('normal')
elif(imc >= 25 and imc < 30):
  print('aobrepeso')
elif(imc >= 30 and imc < 40):
  print('obesidade')
else:
  print('obesidade grave')