"""
Crie um script em Python que escreva dados em um arquivo CSV. 
O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import csv

# Tenta criar o arquivo CSV
try:
    # Abre o arquivo para escrita
    with open('pessoas.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        
        # Escreve o cabeçalho
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        
        # Escreve os dados das pessoas
        escritor.writerow(['Ana Silva', '25', 'São Paulo'])
        escritor.writerow(['João Santos', '30', 'Rio de Janeiro'])
        escritor.writerow(['Maria Oliveira', '22', 'Belo Horizonte'])
        escritor.writerow(['Pedro Costa', '28', 'Porto Alegre'])
        escritor.writerow(['Carla Souza', '35', 'Brasília'])
    
    print("Arquivo CSV criado com sucesso!")
    print("Foram adicionadas 5 pessoas ao arquivo 'pessoas.csv'.")

except Exception as erro:
    print(f"Erro ao criar o arquivo: {erro}")
