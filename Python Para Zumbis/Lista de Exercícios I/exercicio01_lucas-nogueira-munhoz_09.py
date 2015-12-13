kms_percorridos = float(input("Digite a quantidade de kms percorridos : "))
dias = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
preco_dia = 60.00
preco_km = 0.15
total_aluguel = (preco_dia * dias) + (preco_km * kms_percorridos)
print("O total a pagar pelo aluguel do carro sera %.2f reais" %total_aluguel)
