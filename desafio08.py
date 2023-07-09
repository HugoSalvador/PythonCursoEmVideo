metros = int(input('Informe o valor em metros: '))
centimetros = metros*100
milimetros = metros*1000
dm = metros *100
km = metros / 1000
hm = metros / 100
dam = metros / 10

print('O valor de {} metros em centímentros é {}cm e em milimitros é {}mm !'.format(metros, centimetros, milimetros))

#desafio02
print('KM {} \n HM{} \n DAM {}\n M {}\n DM {}\n CM {}\n MM {}'.format(km, hm, dam, metros, dm, centimetros, milimetros))


