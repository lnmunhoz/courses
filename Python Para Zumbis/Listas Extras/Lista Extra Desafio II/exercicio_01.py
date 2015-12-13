# Questão A)
def total_alunos(total_grana):
    alunos = 0
    while total_grana >= 5:
        total_grana -= 5 if total_grana % 7 != 0 else 7
        alunos += 1
    return alunos
print("A) Total de Alunos: %d" %total_alunos(93))
