"""
1- Crie um programa que gera uma senha aleatória com o módulo random, utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""
import random
import string

while True:
    try:
        print("\n=== GERADOR DE SENHAS ALEATÓRIAS ===")
        tamanho = input("Informe a quantidade de caracteres da senha (ou 'sair' para encerrar): ")

        # Permite sair do loop
        if tamanho.lower() == 'sair':
            print("\nEncerrando o programa... Até mais!")
            break

        # Converte o tamanho para inteiro
        tamanho = int(tamanho)

        # Verifica se o tamanho é válido
        if tamanho <= 0:
            raise ValueError("O tamanho da senha deve ser maior que zero.")

        # Conjunto de caracteres possíveis
        caracteres = string.ascii_letters + string.digits + string.punctuation

        # Gera a senha
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        print("→ Sua senha aleatória é:", senha)

    except ValueError as erro:
        print(f"Erro: {erro}. Tente novamente.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}. Tente novamente.")

    finally:
        print("-" * 40)


"""
2- Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
O programa deve exibir o nome, email e país do usuário gerado.
"""
import requests

def gerar_usuario_aleatorio():
    try:
        url = "https://randomuser.me/api/"
        print("Gerando usuário aleatório...\n")
        response = requests.get(url)
        
        if response.status_code == 200:
            dados = response.json()
            usuario = dados['results'][0]
            
            nome_completo = f"{usuario['name']['title']} {usuario['name']['first']} {usuario['name']['last']}"
            email = usuario['email']
            pais = usuario['location']['country']
            
            print("=" * 50)
            print("PERFIL DE USUÁRIO GERADO")
            print("=" * 50)
            print(f"Nome:  {nome_completo}")
            print(f"Email: {email}")
            print(f"País:  {pais}")
            print("=" * 50)
        else:
            print(f"Erro ao acessar a API. Código: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    gerar_usuario_aleatorio()

"""
3- Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""
import requests

while True:
    print("\n=== CONSULTA DE CEP ===")
    cep = input("Digite o CEP (ou 'sair' para encerrar): ")
    
    if cep.lower() == 'sair':
        print("Até logo!")
        break
    
    # Limpa o CEP
    cep = cep.replace("-", "").replace(" ", "").replace(".", "")
    
    # Verifica se tem 8 números
    if len(cep) != 8 or not cep.isdigit():
        print("CEP inválido! Digite 8 números.")
        continue
    
    try:
        # Faz a consulta
        url = f"https://viacep.com.br/ws/{cep}/json/"
        resposta = requests.get(url, timeout=5)  # 5 segundos de timeout
        dados = resposta.json()
        
        if "erro" not in dados:
            print("\nENDEREÇO ENCONTRADO:")
            print(f"{dados['logradouro']}")
            print(f"{dados['bairro']}")
            print(f"{dados['localidade']} - {dados['uf']}")
            print(f"CEP: {dados['cep']}")
        else:
            print("CEP não encontrado!")
             
    except requests.exceptions.Timeout:
        print("Demorou muito! Tente novamente.")
    
    except:
        print("Erro ao consultar o CEP!")



"""
4- Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, máximo e mínimo da cotação, além da data e hora da última atualização. Utilize a API da AwesomeAPI para obter os dados de cotação.
"""
import requests

# Solicita o código da moeda ao usuário
moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()

# Monta a URL da API AwesomeAPI
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

# Faz a requisição
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    dados = response.json()
    chave = f"{moeda}BRL"

    # Verifica se a moeda existe nos dados retornados
    if chave in dados:
        cotacao = dados[chave]
        print("\n=== Cotação Atual ===")
        print(f"Moeda: {cotacao['code']} / {cotacao['codein']}")
        print(f"Valor atual: R$ {float(cotacao['bid']):.2f}")
        print(f"Valor máximo: R$ {float(cotacao['high']):.2f}")
        print(f"Valor mínimo: R$ {float(cotacao['low']):.2f}")
        print(f"Data e hora da última atualização: {cotacao['create_date']}")
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar a API.")
