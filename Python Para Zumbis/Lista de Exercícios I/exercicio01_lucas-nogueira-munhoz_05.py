preco = float(input("Insira o preco da mercadoria : "))
desconto = int(input("Insira o valor do desconto: "))
total = preco - ((preco / 100) * desconto)
print("Valor da mercadoria com desconto = %.0f" %total)
