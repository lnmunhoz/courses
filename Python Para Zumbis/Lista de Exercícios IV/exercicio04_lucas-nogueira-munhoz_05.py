import string

def in_python(word):
	for letter in word:
		if letter.lower() in 'python':
			return True
	return False

texto = open('texto.txt', 'r')
lista = []
for linha in texto.readlines():
	for x in string.punctuation:
		linha = linha.replace(x, "")

	palavras = linha.split()
	for palavra in palavras:
		if len(palavra) > 4:
			if in_python(palavra):
				lista.append(palavra)

print(lista)