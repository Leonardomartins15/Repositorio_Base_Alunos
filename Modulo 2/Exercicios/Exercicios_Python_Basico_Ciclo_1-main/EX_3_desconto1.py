# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
produto = input("Digite o nome do produto :")
porcentagem = float (input("Qual a porcentagem de desconto?"))
preco_produto = float(input(" Qual o preço do produto?"))
desconto = preco_produto * (porcentagem / 100)
preco_final = preco_produto - desconto

print(f"O preço do produto é :{preco_produto}")
print(f"A porcentagem de desconto é :{porcentagem}")
print(f"O produto que custa R${preco_produto} terá R${desconto} de desconto e custará {preco_final}")
