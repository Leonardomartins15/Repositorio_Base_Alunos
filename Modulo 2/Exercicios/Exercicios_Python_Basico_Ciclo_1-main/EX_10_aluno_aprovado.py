# Escreva um código que pede a nota de duas provas do aluno e verifique se o aluno foi aprovado com as condições abaixo:
# O aluno precisa ter média maior que 7 e não pode ter tirado zero em nenhuma nota.
# Não é necessário usar estruturas condicionais, apenas expressões lógicas conforme estudado no material de expressões lógicas.

# OUTPUT ESPERADO:
# Exemplo 1:

# Digite a primeira nota: 10
# Digite a segunda nota: 8
# Aluno aprovado? True

# Exemplo 2:

# Digite a primeira nota: 10
# Digite a segunda nota: 0
# Aluno aprovado? False

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome_aluno = input("Digite o nome do aluno:")
nota1 = float(input("Digite a nota da primeira prova :"))
nota2 = float(input("Digite a nota da segunda prova :"))
media = (nota1 + nota2) / 2

if media <= 7 :
    print(f"Aluno aprovado? false")

else :
    print(f"Aluno aprovado? true")