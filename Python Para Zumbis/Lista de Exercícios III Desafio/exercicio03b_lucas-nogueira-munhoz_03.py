n = int(input('N: '))
if n < 0:
	print("Apenas positivos")
else:
	cont = 0
	if n == 1:
		print ("Primo")
	else:
		
		for i in range(1, n + 1):
			if n % i == 0:
				cont += 1
		if cont == 2:
			print("Primo")
		else:
			print("Nao Primo")
