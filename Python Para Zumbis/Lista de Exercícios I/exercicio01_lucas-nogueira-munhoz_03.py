dias = int(input("Insira a quantidade de dias: ")) 
horas = int(input("Insira a quantiadade de horas: "))
minutos = int(input("Insira a quantidade de minutos: "))
segundos = int(input("Insira a quantidade de segundos :"))
dias_em_segundos = (dias * 24) * (60 * 60)
horas_em_segundos = (horas * 60 * 60)
minutos_em_segundos = (minutos * 60)
total_em_segundos = dias_em_segundos + horas_em_segundos + minutos_em_segundos + segundos
print("Totao de segundos : ", total_em_segundos)

