# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome_aluno = input("Digite o nome do aluno:")
nota1 = float(input("Digite a nota da prova :"))
nota2 = float(input("Digite a nota da prova :"))
nota3 = float(input("Digite a nota da prova :"))
media = (nota1 + nota2 + nota3) / 3



print(f"| ______________________________ |")
print(f"| SISTEMA DE PROVAS")
print(f"| ______________________________ |")
print(f"Nome do aluno: {nome_aluno}")
print(f"Nota da primeira prova : {nota1}")
print(f"Nota da segunda prova : {nota2}")
print(f"Nota da terçeira prova : {nota3}")
print(f"| ______________________________ |")
print(f"Aluno : {nome_aluno}")
print(f"Média : {media:.2f}")

if media >= 7 :
    print(f"Aprovado")

elif media <= 6 :
    print(f"Recuperação")

else :
    print(f"Suspenso")

print(f"| ______________________________ |") 
