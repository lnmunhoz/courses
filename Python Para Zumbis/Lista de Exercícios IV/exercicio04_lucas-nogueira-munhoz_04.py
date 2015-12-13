import string

texto = open('texto.txt', 'r')
lista = []
for linha in texto.readlines():
	for x in string.punctuation:
		linha = linha.replace(x, "")

	palavras = linha.split();
	for palavra in palavras:
		if palavra[0].lower() in 'python' or palavra[-1].lower() in 'python':
			lista.append(palavra)
print(lista)