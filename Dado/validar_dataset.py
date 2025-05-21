import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Carregar o dataset
dataset = pd.read_csv('dataset_aprovacao_credito.csv')

# Criar diretório para as visualizações
os.makedirs('visualizacoes', exist_ok=True)

# 1. Análise de estatísticas básicas
print("Dimensões do dataset:", dataset.shape)
print("\nInformações do dataset:")
print(dataset.info())
print("\nEstatísticas descritivas:")
estatisticas = dataset.describe(include='all')
print(estatisticas)
estatisticas.to_csv('visualizacoes/estatisticas_descritivas.csv')

# 2. Verificar valores ausentes
print("\nValores ausentes por coluna:")
valores_ausentes = dataset.isnull().sum()
print(valores_ausentes)

# 3. Distribuição das variáveis categóricas
print("\nDistribuição da variável 'trabalho':")
dist_trabalho = dataset['trabalho'].value_counts()
print(dist_trabalho)
dist_trabalho.to_csv('visualizacoes/distribuicao_trabalho.csv')

print("\nDistribuição da variável 'credito_aprovado':")
dist_aprovacao = dataset['credito_aprovado'].value_counts()
print(dist_aprovacao)

print("\nDistribuição da variável 'possui_historico_inadimplencia':")
dist_inadimplencia = dataset['possui_historico_inadimplencia'].value_counts()
print(dist_inadimplencia)

print("\nDistribuição da variável 'possui_outros_emprestimos':")
dist_outros_emprestimos = dataset['possui_outros_emprestimos'].value_counts()
print(dist_outros_emprestimos)

# 4. Visualizações para variáveis categóricas
plt.figure(figsize=(10, 6))
sns.countplot(data=dataset, x='trabalho')
plt.title('Distribuição por Tipo de Trabalho')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_trabalho.png')

plt.figure(figsize=(8, 5))
sns.countplot(data=dataset, x='credito_aprovado')
plt.title('Distribuição de Aprovação de Crédito')
plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_aprovacao.png')

# 5. Distribuição das variáveis numéricas
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.histplot(dataset['renda_mensal'], kde=True)
plt.title('Distribuição de Renda Mensal')

plt.subplot(2, 2, 2)
sns.histplot(dataset['idade'], kde=True)
plt.title('Distribuição de Idade')

plt.subplot(2, 2, 3)
sns.histplot(dataset['score_credito'], kde=True)
plt.title('Distribuição de Score de Crédito')

plt.subplot(2, 2, 4)
sns.histplot(dataset['valor_solicitado'], kde=True)
plt.title('Distribuição de Valor Solicitado')

plt.tight_layout()
plt.savefig('visualizacoes/distribuicao_variaveis_numericas.png')

# 6. Correlação entre variáveis numéricas
variaveis_numericas = ['renda_mensal', 'renda_anual', 'idade', 'score_credito', 
                       'tempo_emprego_atual', 'valor_solicitado', 'valor_aprovado']
correlacao = dataset[variaveis_numericas].corr()
print("\nMatriz de correlação:")
print(correlacao)
correlacao.to_csv('visualizacoes/matriz_correlacao.csv')

plt.figure(figsize=(10, 8))
sns.heatmap(correlacao, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Matriz de Correlação entre Variáveis Numéricas')
plt.tight_layout()
plt.savefig('visualizacoes/matriz_correlacao.png')

# 7. Relação entre aprovação de crédito e outras variáveis
plt.figure(figsize=(12, 10))

plt.subplot(2, 2, 1)
sns.boxplot(x='credito_aprovado', y='renda_mensal', data=dataset)
plt.title('Renda Mensal vs. Aprovação de Crédito')

plt.subplot(2, 2, 2)
sns.boxplot(x='credito_aprovado', y='score_credito', data=dataset)
plt.title('Score de Crédito vs. Aprovação de Crédito')

plt.subplot(2, 2, 3)
sns.boxplot(x='credito_aprovado', y='idade', data=dataset)
plt.title('Idade vs. Aprovação de Crédito')

plt.subplot(2, 2, 4)
sns.boxplot(x='credito_aprovado', y='tempo_emprego_atual', data=dataset)
plt.title('Tempo de Emprego vs. Aprovação de Crédito')

plt.tight_layout()
plt.savefig('visualizacoes/relacao_aprovacao_variaveis.png')

# 8. Verificar consistência entre renda mensal e anual
plt.figure(figsize=(8, 6))
sns.scatterplot(x='renda_mensal', y='renda_anual', data=dataset)
plt.title('Relação entre Renda Mensal e Renda Anual')
plt.tight_layout()
plt.savefig('visualizacoes/relacao_renda_mensal_anual.png')

# 9. Verificar consistência entre idade e data de nascimento
# Converter data de nascimento para idade e comparar com a coluna idade
from datetime import datetime

def calcular_idade(data_nascimento):
    try:
        data = datetime.strptime(data_nascimento, '%d/%m/%Y')
        hoje = datetime.now()
        idade = hoje.year - data.year - ((hoje.month, hoje.day) < (data.month, data.day))
        return idade
    except:
        return None

dataset['idade_calculada'] = dataset['data_nascimento'].apply(calcular_idade)
diferenca_idade = (dataset['idade'] - dataset['idade_calculada']).abs()
print("\nDiferença média entre idade e idade calculada:", diferenca_idade.mean())
print("Máxima diferença entre idade e idade calculada:", diferenca_idade.max())

# 10. Verificar consistência entre aprovação e valor aprovado
inconsistencias_aprovacao = ((dataset['credito_aprovado'] == 'Sim') & (dataset['valor_aprovado'] == 0)) | \
                           ((dataset['credito_aprovado'] == 'Não') & (dataset['valor_aprovado'] > 0))
print("\nNúmero de inconsistências entre aprovação e valor aprovado:", inconsistencias_aprovacao.sum())

# 11. Verificar se há valores extremos ou outliers
plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
sns.boxplot(y='renda_mensal', data=dataset)
plt.title('Boxplot de Renda Mensal')

plt.subplot(2, 2, 2)
sns.boxplot(y='valor_solicitado', data=dataset)
plt.title('Boxplot de Valor Solicitado')

plt.subplot(2, 2, 3)
sns.boxplot(y='score_credito', data=dataset)
plt.title('Boxplot de Score de Crédito')

plt.subplot(2, 2, 4)
sns.boxplot(y='valor_aprovado', data=dataset)
plt.title('Boxplot de Valor Aprovado')

plt.tight_layout()
plt.savefig('visualizacoes/boxplots_outliers.png')

# 12. Resumo da validação
print("\n=== RESUMO DA VALIDAÇÃO ===")
print(f"Total de registros: {len(dataset)}")
print(f"Variáveis categóricas: {dataset.select_dtypes(include=['object']).columns.tolist()}")
print(f"Variáveis numéricas: {dataset.select_dtypes(include=['number']).columns.tolist()}")
print(f"Taxa de aprovação: {dataset['credito_aprovado'].value_counts(normalize=True)['Sim']*100:.2f}%")
print(f"Valores ausentes: {dataset.isnull().sum().sum()}")
print(f"Inconsistências entre aprovação e valor: {inconsistencias_aprovacao.sum()}")
print(f"Diferença média entre idade e idade calculada: {diferenca_idade.mean():.2f}")

# Salvar o resumo em um arquivo
with open('visualizacoes/resumo_validacao.txt', 'w') as f:
    f.write("=== RESUMO DA VALIDAÇÃO ===\n")
    f.write(f"Total de registros: {len(dataset)}\n")
    f.write(f"Variáveis categóricas: {dataset.select_dtypes(include=['object']).columns.tolist()}\n")
    f.write(f"Variáveis numéricas: {dataset.select_dtypes(include=['number']).columns.tolist()}\n")
    f.write(f"Taxa de aprovação: {dataset['credito_aprovado'].value_counts(normalize=True)['Sim']*100:.2f}%\n")
    f.write(f"Valores ausentes: {dataset.isnull().sum().sum()}\n")
    f.write(f"Inconsistências entre aprovação e valor: {inconsistencias_aprovacao.sum()}\n")
    f.write(f"Diferença média entre idade e idade calculada: {diferenca_idade.mean():.2f}\n")

print("\nValidação concluída! Resultados salvos no diretório 'visualizacoes'.")
