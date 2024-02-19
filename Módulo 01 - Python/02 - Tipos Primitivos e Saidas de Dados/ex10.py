real = float(input('Quanto dinheiro você tem? '))
dolar = real / 4.87
euro = real / 5.34
libra = real / 6.22
print('Com R${:.2f} você tem direito a U${:.2f} de acordo com a cotação do dia de hoje'.format(real, dolar))
print('Com R${:.2f} você tem direito a €{:.2f} de acordo com a cotação do dia de hoje.'.format(real, euro))
print('Com R${:.2f} você tem direito a &{:.2f} de acordo com a cotação do dia de hoje.'.format(real, libra))
print('Fonte: www.google.com')