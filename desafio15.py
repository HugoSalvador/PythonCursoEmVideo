qtdDias = float(input('Informe a quantidade de dias pelo quaul ele foi alugado: '))
kmPercorrido = float(input('Informe a quantidade de KM percorrido: '))

totalDias = qtdDias * 60
totalKm = kmPercorrido * 0.15
totalAluguel = totalDias + totalKm

print('O total de dias {} custa R${}'.format(qtdDias, totalDias))
print('Você percorreu {}KM o preço da gasolina ficou R${:.2f}'.format(kmPercorrido, totalKm))
print('Total do aluguel R$: {} '.format(totalAluguel))

#solucao do curso
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
