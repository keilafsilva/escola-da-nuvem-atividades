"""
1 - Área da Circunferência
 A fórmula para calcular a área de uma circunferência é: área = π × raio².
 Considerando para este problema que π = 3.14159265:
 Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

 Entrada:
 A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio.

 Saída:
 Apresente a mensagem "A=" seguido pelo valor da variável área, conforme exemplo abaixo,
 com 4 casas após o ponto decimal.
"""

raio = float(input("Digite o valor do raio: "))
PI = 3.14159265
area = PI * (raio**2)

print(f"A={area:.4f}")


"""
2 - Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o em uma das seguintes categorias:
Criança (0-12 anos)
Adolescente (13-17 anos)
Adulto (18-59 anos)
Idoso (60 anos ou mais)
"""

idade = int(input("Digite sua idade: "))
if idade < 0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

"""
 3 - Calculadora de IMC
 Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
 O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
 calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

 < 18.5: classificacao = "Abaixo do peso"
 < 25: classificacao = "Peso normal"
 < 30: classificacao = "Sobrepeso"
 Para os demais cenários: classificacao = "Obeso"
"""
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return imc, "Abaixo do peso"
    elif imc < 25:
        return imc, "Peso normal"
    elif imc < 30:
        return imc, "Sobrepeso"
    else:
        return imc, "Obeso"

altura = float(input("Digite sua altura (m): "))
peso = float(input("Digite seu peso (kg): "))
imc, classificacao = calcular_imc(peso, altura)
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")


"""
 4 - Conversor de Temperatura
 Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
 O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

def converter_temperatura(temperatura, origem, destino):
    if origem == "C":
        celsius = temperatura
    elif origem == "F":
        celsius = (temperatura - 32) * 5 / 9
    elif origem == "K":
        celsius = temperatura - 273.15
    else:
        raise ValueError("Unidade de origem inválida.")

    if destino == "C":
        return celsius
    elif destino == "F":
        return (celsius * 9 / 5) + 32
    elif destino == "K":
        return celsius + 273.15
    else:
        raise ValueError("Unidade de destino inválida.")

while True:
    try:
        temperatura = float(input("Digite a temperatura: "))
        break  
    except ValueError:
        print("Erro: digite um número válido para a temperatura.")

while True:
    try:
        origem = input("Informe a unidade de origem (C, F ou K): ").upper()
        if origem not in ["C", "F", "K"]:
            raise ValueError("Unidade de origem inválida.")
        break
    except ValueError as e:
        print("Erro:", e)

while True:
    try:
        destino = input("Informe a unidade de destino (C, F ou K): ").upper()
        if destino not in ["C", "F", "K"]:
            raise ValueError("Unidade de destino inválida.")
        break
    except ValueError as e:
        print("Erro:", e)

try:
    resultado = converter_temperatura(temperatura, origem, destino)
    print(f"{temperatura:.2f}°{origem} = {resultado:.2f}°{destino}")
except Exception:
    print("Ocorreu um erro inesperado durante a conversão.")

"""
 5 - Verificador de Ano Bissexto
 Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.# Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100)
 que não são divisíveis por 400.
"""

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")

"""
 6 - Calculadora de Comissão
 Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
 efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
 sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
 
 Entrada:
 O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão
 (double) com duas casas decimais, representando o salário fixo do vendedor e o montante total
 das vendas efetuadas por este vendedor, respectivamente.

 Saída:
 Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: R$ "))
total_vendas = float(input("Digite o total de vendas do mês: R$ "))

comissao = total_vendas * 0.15

total_a_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_a_receber:.2f}")

"""
 7 - Calculadora da Média
 Faça um programa que leia quatro números (N1, N2, N3, N4),
 cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
 Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas
 e mostre esta média acompanhada pela mensagem "Media: ".

 Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.".
 Se a média calculada for inferior a 5.0, imprima a mensagem "Aluno reprovado.".
 Se a média calculada for um valor entre 5.0 e 6.9, inclusive estas,
 o programa deve imprimir a mensagem "Aluno em exame.".

 No caso do aluno estar em exame, leia um valor correspondente à nota do exame obtida pelo aluno.
 Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada.
 Recalcule a média (some a pontuação do exame com a média anteriormente calculada e divida por 2)
 e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais)
 ou "Aluno reprovado." (caso a média tenha ficado 4.9 ou menos).

 Para estes dois casos (aprovado ou reprovado após ter pego exame),
 apresente na última linha uma mensagem "Media final: " seguido da média final para esse aluno.

 Entrada:
 A entrada contém quatro números de ponto flutuante correspondentes às notas dos alunos.

 Saída:
 Todas as respostas devem ser apresentadas com uma casa decimal.
 As mensagens devem ser impressas conforme a descrição do problema.
 Não esqueça de imprimir o enter após o final de cada linha, caso contrário obterá "Presentation Error".
"""
while True:
    try:
        N1 = float(input("Digite a primeira nota: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, a nota do aluno.")
while True:
    try:
        N2 = float(input("Digite a segunda nota: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, a nota do aluno.")
while True:
    try:
        N3 = float(input("Digite a terceira nota: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, a nota do aluno.")
while True:
    try:
        N4 = float(input("Digite a quarta nota: "))
        break
    except ValueError:
        print("Entrada inválida! Por favor, a nota do aluno.")

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2

    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")



