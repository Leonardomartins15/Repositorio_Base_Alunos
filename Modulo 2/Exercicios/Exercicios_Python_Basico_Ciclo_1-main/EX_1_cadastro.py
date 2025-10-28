# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

nome_usuario = input("Digite seu nome :")
idade = input("Digite seu idade :")
email = input("Digite seu e-mail :")
senha = input("Digite sua senha :")

print("| ------------------------------ |")
print("| ---------- CADASTRO ---------- |")
print("| ------------------------------ |")
print(f"nome: {nome_usuario} ")
print(f"Idade : {idade}") 
print(f"Email : {email}")
print(f"Senha : {senha}")
