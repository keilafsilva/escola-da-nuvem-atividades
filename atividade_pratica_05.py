"""
Atividade Prática 05
"""

"""
1- Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de gorjeta desejada. 
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada
"""

def calcula_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

try:
    valor_conta = float(input("Digite o valor da conta: "))
    porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta: "))
    
    resultado = calcula_gorjeta(valor_conta, porcentagem_gorjeta)
    print(f"A gorjeta é R$ {resultado:.2f}")

except ValueError:
    print("Entrada inválida! Por favor, digite um número válido.")

"""
2- Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def eh_palindromo(texto):
    texto = texto.lower()             
    texto = texto.replace(" ", "")     
    if texto == texto[::-1]:           
        return "Sim"
    else:
        return "Não"

print(eh_palindromo("arara"))
print(eh_palindromo("Olá, mundo"))


"""
3- Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço 
final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 
Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcula_produto_com_desconto(valor_produto, porcentagem_desconto):
    return valor_produto - (valor_produto * (porcentagem_desconto / 100))

try:
    valor_produto = float(input("Digite o valor do produto: "))
    porcentagem_desconto = float(input("Digite a porcentagem de desconto: "))
    
    resultado = calcula_produto_com_desconto(valor_produto, porcentagem_desconto)
    print(f"O valor do produto com desconto é R$ {resultado:.2f}")

except ValueError:
    print("Entrada inválida! Por favor, digite um número válido.")


"""
4- Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""

def calcula_idade_em_dias(ano_nascimento):
    ano_atual = 2025 
    idade_em_anos = ano_atual - ano_nascimento
    anos_bissextos = idade_em_anos // 4 
    idade_em_dias_precisa = (idade_em_anos * 365) + anos_bissextos
    return idade_em_dias_precisa

try:
    ano_nascimento = int(input("Digite um ano de nascimento: "))
    resultado = calcula_idade_em_dias(ano_nascimento)
    print(f"A dia idade em dias é {resultado:.2f}")


except ValueError:
    print("Entrada inválida! Por favor, digite um número válido.")

