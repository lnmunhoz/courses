import random
lista = []
while len(lista) < 10:
	lista.append(random.randint(1, 100))
print(lista)

maior = lista[0]
menor = lista[0]

for i in lista:
	if i >= maior:
		maior = i
	if i <= menor:
		menor = i

print("Maior: %d" %maior)
print("Menor: %d" %menor)
