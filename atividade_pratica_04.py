"""
 1 - Calculadora com tratamento de erros

 Desenvolva uma calculadora em Python que realize as quatro operações básicas
 (adição, subtração, multiplicação e divisão) entre dois números.

 Especificações:
 - Solicitar ao usuário dois números e uma operação.
 - Operações válidas: +, -, *, /
 - O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

 Tratar os seguintes erros com try/except:
 - Entrada inválida (não numérica)
 - Divisão por zero
 - Operação inválida

 Após cada erro, o programa deve informar o usuário e pedir nova entrada.
 Quando uma operação for concluída com sucesso, exibir o resultado e encerrar o programa.
 ==============================================================
 Calculadora com repetição de entradas até serem válidas
"""

while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Entrada inválida! Digite apenas números.")

while True:
    operacao = input("Digite uma operação válida (+, -, *, /): ")

    if operacao == "+":
        resultado = num1 + num2
        break
    elif operacao == "-":
        resultado = num1 - num2
        break
    elif operacao == "*":
        resultado = num1 * num2
        break
    elif operacao == "/":
        try:
            resultado = num1 / num2
        except ZeroDivisionError:
            print("Erro: divisão por zero não é permitida. Tente outra operação.")
            continue  
        break
    else:
        print("Operação inválida! Tente novamente.")

print(f"Resultado = {resultado}")

"""
 2 - Registro de notas e cálculo da média

 Crie um programa que permita a um professor registrar as notas de uma turma.

 Especificações:
 - O programa deve continuar solicitando notas até que o professor digite 'fim'.
 - Notas válidas: de 0 a 10.
 - Notas inválidas devem ser ignoradas (e o programa continua solicitando).
 - No final, exibir a média da turma.
"""

cont = 0
soma = 0

while True:
    entrada = input(f"Digite a nota do aluno {cont + 1} ou 'fim' para terminar: ")

    if entrada.lower() == 'fim':
        if cont > 0:
            media = soma / cont
            print("\nResumo:")
            print(f"A média da turma é = {media:.2f}")
        else:
            print("Nenhuma nota válida foi registrada.")
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            soma += nota
            cont += 1
        else:
            print("Entrada inválida! A nota deve ser de 0 a 10 ou 'fim' para terminar.")
    except ValueError:
        print("Entrada inválida! A nota deve ser de 0 a 10 ou 'fim' para terminar.")

"""
 ==============================================================
 3 - Verificador de senha forte
 ==============================================================

 Crie um programa que verifique se uma senha é forte.

 Regras:
 - A senha deve ter pelo menos 8 caracteres.
 - Deve conter pelo menos um número.

 O programa deve continuar pedindo senhas até que uma senha válida seja inserida
 ou até que o usuário digite 'sair'.
"""

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")
    
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    if len(senha) < 8:
        print("Senha fraca: precisa ter pelo menos 8 caracteres.")
        continue
    
    if not any(char.isdigit() for char in senha):
        print("Senha fraca: precisa conter pelo menos um número.")
        continue
    
    print("Senha válida e forte!")
    break

"""
 4 - Verificador de número par ou ímpar

 Crie um programa que solicite ao usuário que insira números inteiros.

 Especificações:
 - O programa deve continuar solicitando números até que o usuário digite 'fim'.
 - Para cada número, informar se é par ou ímpar.
 - Se o usuário inserir algo que não seja um número inteiro,
   o programa deve informar o erro e continuar pedindo.
 - No final, exibir a quantidade de números pares e ímpares inseridos.
"""

pares = 0
impares = 0

while True:
    entrada = (input("Digite um número ou fim para terminar: "))
    if entrada.lower() == 'fim':
        print("\nResumo:")
        print(f"Quantidade de PARES = {pares}")
        print(f"Quantidade de ÍMPARES = {impares}")
        break
    try:
        if int(entrada) % 2 == 0:
            print(f"{entrada} é PAR")
            pares +=1
        else:
            print(f"{entrada} é ÍMPAR")
            impares +=1
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro ou fim para terminar.")


