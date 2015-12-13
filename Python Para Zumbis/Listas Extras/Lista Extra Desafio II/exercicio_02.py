# Questão B)
def numero_romano(n):
    s = ''
    romanos = ['M', 'D', 'C', 'L', 'X', 'V']
    numeros = [1000, 500, 100, 50, 10, 5]
    for i in range(len(romanos)):
        s += n // numeros[i] * romanos[i]
        n %= numeros[i]
    return s + n * 'I'

print("B) 2013: %s" %numero_romano(2013))
print(numero_romano(89))