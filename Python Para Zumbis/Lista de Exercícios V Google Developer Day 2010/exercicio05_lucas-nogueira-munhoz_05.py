def digitos_unicos(str_n):
	for i in range(len(str_n) - 1):
		if str_n[i] is str_n[i + 1]:
			return False
		i += 1
	return True
		
def soma_par(str_n):
	soma = 0
	for n in str_n:
		soma += int(n)
	return soma % 2 is 0

def primeiro_igual_ultimo(str_n):
	first = str_n[0]
	last = str_n[len(str_n) - 1]
	return first is last

arquivo = open('telefones_ex5.txt', 'r')

for linha in arquivo.readlines():
	telefones = linha.split(" ")
arquivo.close()

validos = 0
for telefone in telefones:
	if digitos_unicos(telefone) and soma_par(telefone):
		if not primeiro_igual_ultimo(telefone):
			validos += 1
print(validos)