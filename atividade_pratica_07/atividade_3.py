"""
3- Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. 
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""
import csv

arquivo = 'pessoas.csv'

try:
    with open(arquivo, 'r', encoding='utf-8') as f:
        # Lê tudo de uma vez
        dados = list(csv.reader(f))
        
        print("Conteúdo do arquivo CSV:")
        for linha in dados:
            print(linha)
            
except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo} não existe!")
    
except:
    print("Algo deu errado na leitura do arquivo.")
