### exercicio dia 2 - calcular o ano de nascimento a partir da idade
nome_pessoa =input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))
print("olá",nome_pessoa,", você nasceu em", 2026 - int(idade))
# atividades do dia 2 (videos yt)
valor1 = int(input("digite o primeiro valor: "))
valor2 = int(input("digite o segundo valor: "))
soma = valor1 + valor2
print("a soma dos valores é: ", soma)
###################################################
print("O tipo primitivo de ", nome_pessoa, "é: ", type(nome_pessoa))
print("O tipo primitivo de ", idade, "é: ", type(idade))
print(nome_pessoa, "tem espaço? ", nome_pessoa.isspace())
print("O nome tem letras? ", nome_pessoa.isalpha())
print("O nome tem números? ", nome_pessoa.isnumeric())
print("O nome tem letras e números? ", nome_pessoa.isalnum())
print("O nome tem letras maiúsculas? ", nome_pessoa.isupper())
print("O nome tem letras minúsculas? ", nome_pessoa.islower())
print("O nome tem a primeira letra maiúscula? ", nome_pessoa.istitle())

