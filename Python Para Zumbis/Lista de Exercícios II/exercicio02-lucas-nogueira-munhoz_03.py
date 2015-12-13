peso = float(input("Peso: "))
multa = 0
if peso > 50:
	multa = (peso - 50) * 4
print("Valor da multa: R$: %2.f" %multa)