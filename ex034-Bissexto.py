#Descobrindo se o ano é bissexto
import datetime
ano=int(input('Digite um ano (digite zero para o ano atual): '))
if ano==0:
    ano=datetime.date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano de {} é um ano bissexto.'.format(ano))
else:
    print('O ano de {} não é um ano bissexto.'.format(ano))
