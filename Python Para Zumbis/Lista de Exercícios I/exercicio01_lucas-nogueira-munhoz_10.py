print("Calculo de tempo de vida de um fumante.")
cigarros_por_dia = int(input("Insira a quantidade de cigarros que voce fuma por dia: "))
anos_fumante = int(input("Insira a quantidade de anos que voce ja fuma: "))
total_dias = 365 * anos_fumante
dias_perdidos = ((total_dias * cigarros_por_dia * 10) / 60) /24
print("Voce ja perdeu %d dias de vida." %dias_perdidos)
