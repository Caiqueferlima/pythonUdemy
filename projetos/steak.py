steak = int(input('Qual a temperatura da carne? '))

if(steak < 48):
  print('Crua')
elif(steak >= 48 and steak < 54):
  print('selada')
elif(steak >= 54 and steak < 60):
  print('selada')
elif(steak >= 60 and steak < 65):
  print('selada')
elif(steak >= 65 and steak < 71):
  print('selada')
else:
  print('Bem passada')
