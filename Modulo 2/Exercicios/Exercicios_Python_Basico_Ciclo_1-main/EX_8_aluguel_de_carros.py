# Aluguel de carros:
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado

# OUTPUT ESPERADO:

# Por quantos dias o carro foi alugado: 10
# Quantos km o carro rodou: 500
# Você andou 500.0km por 10 dias, então o preço a pagar é R$675.00.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

#Aluguel de Carro

quantidade_km = float(input("Qual foi a quantidade de KM percorrido pelo carro alugado ?"))
dias = int(input("Quantos dias ele foi alugado ?"))
custos_dias = 60.0 # valor por dia 
km_por_rodada = 0.15 # valor por km rodado
preco_a_pagar = (dias * custos_dias) + (quantidade_km * km_por_rodada)

print(f"Você andou {quantidade_km} Km por {dias} dias, então o preço a pagar é {preco_a_pagar}")

