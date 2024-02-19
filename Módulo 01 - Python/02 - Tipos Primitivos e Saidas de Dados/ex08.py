medida = float(input ('Distância em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida * 0.001
print('A medida de {}m corresponde a {:.0f}cm, {:.0f}mm, e {}km'.format(medida, cm, mm, km))