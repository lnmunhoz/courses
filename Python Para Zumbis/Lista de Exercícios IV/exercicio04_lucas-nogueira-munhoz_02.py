import random
lista = []
pares = []
impares = []
while len(lista) < 20:
	lista.append(random.randint(1, 100))
for i in lista:
	if i % 2 == 0:
		pares.append(i)
	else:
		impares.append(i)

print("Lista: ", lista)
print("Pares: ", pares)
print("Impares: ", impares)