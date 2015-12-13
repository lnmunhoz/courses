valor = int(input('Conta: '))
pagamento = int(input('Pagamento: '))
notas = [50, 20, 10, 5, 2, 1]
notas_troco = []
if pagamento < valor:
	print('Pagamento precisa ser maior que valor')
else:
	troco = pagamento - valor
	i = 0
	while troco > 0:
		if troco - notas[i] >= 0:
			troco -= notas[i]
			notas_troco.append(notas[i])
		else:
			i += 1
print(notas_troco)
