a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

maior = 0

if a >= b and a >= c:
	maior = a
elif b > c:
	maior = b
else:
	maior = c
print("Maior: %d" %maior) 