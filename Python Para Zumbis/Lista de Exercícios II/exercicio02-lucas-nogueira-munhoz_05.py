a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
maior = 0
menor = 0
if a >= b and a >= c:
	maior = a
	if b >= c:
		menor = c
	else:
		menor = b
elif b >= c:
	maior = b
	if a >= c:
		menor = c
	else:
		menor = a
else:
	maior = c
	if a >= b:
		menor = b
	else:
		menor = a

print("Maior: %d" %maior) 
print("Menor: %d" %menor)