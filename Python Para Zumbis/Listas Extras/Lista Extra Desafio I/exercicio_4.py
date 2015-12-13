
# Questao D)
def calc_graos(casas_tabuleiro):
  total = 1
  prev = 1
  for i in range(casas_tabuleiro):
    total += prev * 2
    prev *= 2
  return total

print("Total de Graos:", calc_graos(64))