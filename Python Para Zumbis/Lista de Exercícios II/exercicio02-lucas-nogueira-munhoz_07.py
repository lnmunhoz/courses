area = float(input("Area em metros quadrados: "))
litros = area / 3
valor = 0

if litros % 18 == 0:
	valor = litros / 18 * 80
else:
	valor = int((litros / 18 + 1)) * 80
print ("Valor %2.f" %valor)