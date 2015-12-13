# Questao C)
def calc_pi(n_termos):
  result = 0
  divisor = 1
  for i in range(n_termos):
    result += (4 / divisor) if i % 2 == 0 else -(4 / divisor)
    divisor += 2
  return result
print ("C) 4 Termos:", calc_pi(4))
print (calc_pi(100000))