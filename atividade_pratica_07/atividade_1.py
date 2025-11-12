"""
1- Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""
import pandas as pd

# Lê o arquivo CSV (certifique-se de que o arquivo esteja na mesma pasta do seu script)
base = pd.read_csv('log_treinamento.csv')

# Calcula média e desvio padrão da coluna 'tempo_execucao'
media = base['tempo_execucao'].mean()
desvio = base['tempo_execucao'].std()

print(f"Média do tempo de execução: {media:.2f}")
print(f"Desvio padrão do tempo de execução: {desvio:.2f}")
