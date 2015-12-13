a = int(input("Lado A"))
b = int(input("Lado B"))
c = int(input("Lado C"))

if a == b and b == c:
	print("Equilatero")
elif a != b and b != c and c != a:
	print("Escaleno")
else:
	print("Isosceles")
