ano = int(input("Digite o ano: "))
if (ano % 400 == 0 or ano % 100 != 0) and ano % 4 == 0:
	print("Bissexto")
else:
	print("Nao Bissexto")