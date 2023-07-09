preco = float(input('Informe o preço do produto: R$'))
precoDesconto = preco - (preco * (5 / 100))
print('O produto com o desconto de 5% sai no preço de R${:.2f}'.format(precoDesconto))
