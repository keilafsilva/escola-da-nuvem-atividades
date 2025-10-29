# -----------------------------------------------------------
# Atividade Prática 01 – Escola da Nuvem
# Linguagem: Python
# Descrição: Exercícios básicos com operações matemáticas e entrada de dados.
# Autora: Keila Fernanda
# -----------------------------------------------------------

# 1- Programa de Saudação
# Crie um programa que imprima a mensagem "Hello, world!" na tela.

print("Hello, world!")


# 2- Calculadora de Soma
# Desenvolva um programa que soma dois números.
# Use as variáveis numero1 = 12 e numero2 = 14. 
# O programa deve calcular a soma e exibir o resultado.

numero1 = 12
numero2 = 14
soma = numero1 + numero2

print(f"A soma de {numero1} e {numero2} é {soma}")


# 3- Calculadora de Volume
# Crie um programa que calcule o volume de uma caixa retangular.
# Use as seguintes dimensões:
# Comprimento: 12 cm
# Largura: 14 cm
# Altura: 20 cm 
# O programa deve calcular o volume e exibir o resultado em cm³.

comprimento = 12
largura = 14
altura = 20

volume = comprimento * largura * altura

print(f"O volume é {volume} cm³")


# 4- Calculadora de Preço Total
# Desenvolva um programa que calcule o preço total de uma compra.
# Use as seguintes informações:
# Nome do produto: "Cadeira Infantil"
# Preço unitário: R$ 12.40
# Quantidade: 3 
# O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.

nomeDoProduto = "Cadeira Infantil"
precoUnitario = 12.40
quantidade = 3 

precoTotal = quantidade * precoUnitario

print("\n=== Resumo da Compra ===")
print(f"Produto: {nomeDoProduto}")
print(f"Preço unitário: R$ {precoUnitario:.2f}")
print(f"Quantidade: {quantidade}")
print(f"Preço total: R$ {precoTotal:.2f}")


# 5- Calculadora de Número Inteiro
# Leia quatro valores inteiros A, B, C e D.
# A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D
# segundo a fórmula: DIFERENCA = (A * B - C * D).

valorA = int(input("\nDigite o valor A: "))
valorB = int(input("Digite o valor B: "))
valorC = int(input("Digite o valor C: "))
valorD = int(input("Digite o valor D: "))

diferenca = (valorA * valorB) - (valorC * valorD)

print(f"DIFERENCA = {diferenca}")
