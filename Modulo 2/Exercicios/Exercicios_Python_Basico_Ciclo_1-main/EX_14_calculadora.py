# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Escolha uma opção:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Divisão")
print("4 - Multiplicação")

opcao = input("Digite a opção :")


if opcao == "1" :
    numero1 = int(input("Digite o número :")) 
    numero2= float(input("Digite o número :"))
    valor = numero1 + numero2
    print(f"resultado da adição foi: {valor:.2f}")

elif opcao == "2" :
    numero1 = int(input("Digite o número :")) 
    numero2= float(input("Digite o número :"))
    valor = numero1 - numero2
    print(f"resultado da subtração foi: {valor:.2f}")

elif opcao == "3" :
    numero1 = int(input("Digite o número :")) 
    numero2= float(input("Digite o número :"))
    valor = numero1 / numero2
    print(f"resultado da divisão foi: {valor:.2f}")

elif opcao == "4" :
    numero1 = int(input("Digite o número :")) 
    numero2= float(input("Digite o número :"))
    valor = numero1 * numero2
    print(f"resultado da multiplicação foi: {valor:.2f}")

else :
   
    print(f"ERRO. Escolha uma opção válida.")


