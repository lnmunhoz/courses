import random
a = []
b =[]
c = []

for i in range(10):
	a.append(random.randint(1, 100))
	b.append(random.randint(1, 100))

for  i in range(9):
		c.append(a[i])
		c.append(b[i])


print(a)
print(b)
print(c)