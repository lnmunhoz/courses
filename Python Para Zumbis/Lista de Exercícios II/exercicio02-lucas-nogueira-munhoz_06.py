valor = float(input("Quando voce ganha por hora? : "))
horas = float(input("Quantas horas voce pra trabalha por mes? : "))
salario_bruto = valor * horas
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato
print("Salario do mes = R$: %2.f" %(salario_liquido))