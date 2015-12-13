

n = int(input("n: "))

if n is 1:
	print(n)
else:
	prev = 0
	fibo = 1
	print(fibo)
	while n > 1:
		aux = fibo
		fibo = fibo + prev
		prev = aux
		n -= 1
		print(fibo)


