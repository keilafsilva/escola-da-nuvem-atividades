"""
4- Crie um script em Python que leia e escreva dados em um arquivo JSON. 
O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""
import json

def ler_arquivo_json(arquivo="dados.json"):
    """
    Lê dados de um arquivo JSON com tratamento de erro
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            dados = json.load(file)
            print("Dados carregados com sucesso!")
            return dados
    except FileNotFoundError:
        print("Arquivo não encontrado. Será criado um novo.")
        return {}
    except json.JSONDecodeError:
        print("Erro: Arquivo JSON inválido ou corrompido.")
        return {}
    except Exception as e:
        print(f"Erro inesperado ao ler arquivo: {e}")
        return {}

def escrever_arquivo_json(dados, arquivo="dados.json"):
    """
    Escreve dados em um arquivo JSON com tratamento de erro
    """
    try:
        with open(arquivo, 'w', encoding='utf-8') as file:
            json.dump(dados, file, ensure_ascii=False, indent=4)
        print("Dados salvos com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
        return False

def main():
    # Lê dados existentes ou cria novo
    dados = ler_arquivo_json()
    
    # Se não há dados, cria estrutura vazia
    if not dados:
        dados = {"pessoas": []}
    
    # Coleta dados da pessoa
    try:
        nome = input("Digite o nome: ").strip()
        if not nome:
            raise ValueError("Nome não pode estar vazio")
        
        idade = int(input("Digite a idade: "))
        if idade < 0 or idade > 150:
            raise ValueError("Idade deve ser entre 0 e 150")
        
        cidade = input("Digite a cidade: ").strip()
        if not cidade:
            raise ValueError("Cidade não pode estar vazia")
            
    except ValueError as e:
        print(f"Erro nos dados: {e}")
        return
    except KeyboardInterrupt:
        print("\nOperação cancelada pelo usuário")
        return
    
    # Cria dicionário com os dados
    pessoa = {
        "nome": nome,
        "idade": idade,
        "cidade": cidade
    }
    
    # Adiciona aos dados existentes
    dados["pessoas"].append(pessoa)
    
    # Salva no arquivo
    escrever_arquivo_json(dados)
    
    # Mostra dados salvos
    print("\nDados salvos:")
    print(f"Nome: {pessoa['nome']}")
    print(f"Idade: {pessoa['idade']}")
    print(f"Cidade: {pessoa['cidade']}")

if __name__ == "__main__":
    main()