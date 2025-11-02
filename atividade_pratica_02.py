# 1- Conversor de Moeda 
# Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
# Valor em reais: R$ 100.00
# Taxa do dólar: R$ 5.60
# Taxa do euro: R$ 6.60 
# O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

valor_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: US$ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}")


# 2- Calculadora de Desconto 
# Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:
# Nome do produto: "Camiseta"
# Preço original: R$ 50.00
# Porcentagem de desconto: 20% 
# O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.

nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_de_desconto = 20

desconto = preco_original * (porcentagem_de_desconto/100)
preco_final = preco_original - desconto

print(f"O produto {nome_do_produto} que custava R${preco_original:.2f}, teve um desconto de R${desconto:.2f}, e o preço final é R${preco_final:.2f}")


# 3- Calculadora de Média Escolar 
# Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
# Nota 1: 7.5
# Nota 2: 8.0
# Nota 3: 6.5 
# O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

nota1 = 7.5
nota2 = 8.0
nota3 = 6.5 

media = (nota1 + nota2 + nota3)/3

print(f"Notas: {nota1}, {nota2}, {nota3} -> Média: {media:.2f}")


# 4- Calculadora de Consumo de Combustível
# Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
# Distância percorrida: 300 km
# Combustível gasto: 25 litros 
# O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

distancia_percorrida = 300 
combustivel_gasto = 25 

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Distância: {distancia_percorrida} km, Combustível gasto: {combustivel_gasto} L, Consumo médio: {consumo_medio:.2f} km/l")


# 5- Calculadora de Soma com Entrada do Usuário
# Leia 2 valores inteiros e armazene-os nas variáveis A e B. 
# Efetue a soma de A e B, atribuindo o seu resultado à variável X. 
# Entrada: A entrada contém 2 valores inteiros informados pelo usuário. 
# Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável X e pelo final de linha.

numb1 = int(input("Digite o primeiro número: "))
numb2 = int(input("Digite o segundo número: "))

soma = numb1 + numb2

print(f"X = {soma}")


# 6- Calculadora de salário por horas trabalhadas
# Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.
# Entrada:
# O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:
# Número do funcionário (numero_funcionario).
# Quantidade de horas trabalhadas (horas_trabalhadas).
# Valor recebido por hora (valor_por_hora).
# Saída:
# Imprima o número do funcionário e o salário calculado com duas casas decimais. Deve haver um espaço em branco antes e depois do sinal de igualdade, e no caso do salário, também um espaço em branco após o R$

numero_funcionario = int(input("Digite o Número do funcionario: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora

print(f"Número do funcionário = {numero_funcionario}")
print(f"Salário = R${salario:.2f}")