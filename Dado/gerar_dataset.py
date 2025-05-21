import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import names
from faker import Faker

# Configurar o faker para português brasileiro sem depender do locale
fake = Faker('pt_BR')

# Função para gerar uma data de nascimento aleatória para pessoas entre 18 e 80 anos
def gerar_data_nascimento():
    hoje = datetime.now()
    idade = random.randint(18, 80)
    data = hoje - timedelta(days=idade*365 + random.randint(0, 364))
    return data.strftime('%d/%m/%Y'), idade

# Função para gerar um nome completo brasileiro
def gerar_nome():
    return fake.name()

# Lista de ocupações profissionais
ocupacoes = [
    "Funcionário Público", 
    "Funcionário de Empresa Privada", 
    "Empresário/Autônomo", 
    "Aposentado/Pensionista", 
    "Profissional Liberal", 
    "Desempregado", 
    "Estudante", 
    "Outros"
]

# Pesos para as ocupações (para tornar algumas mais comuns que outras)
pesos_ocupacoes = [0.15, 0.35, 0.15, 0.12, 0.10, 0.05, 0.05, 0.03]

# Função para gerar renda mensal baseada na ocupação
def gerar_renda_mensal(ocupacao, idade):
    base = 0
    
    if ocupacao == "Funcionário Público":
        base = random.uniform(3000, 15000)
    elif ocupacao == "Funcionário de Empresa Privada":
        base = random.uniform(1500, 12000)
    elif ocupacao == "Empresário/Autônomo":
        base = random.uniform(2000, 30000)
    elif ocupacao == "Aposentado/Pensionista":
        base = random.uniform(1200, 8000)
    elif ocupacao == "Profissional Liberal":
        base = random.uniform(3000, 25000)
    elif ocupacao == "Desempregado":
        base = random.uniform(0, 1000)
    elif ocupacao == "Estudante":
        base = random.uniform(0, 2000)
    else:  # Outros
        base = random.uniform(1000, 5000)
    
    # Ajuste pela idade (experiência)
    fator_idade = min(1.5, max(0.8, idade / 40))
    
    # Adicionar alguma variação
    variacao = random.uniform(0.8, 1.2)
    
    return round(base * fator_idade * variacao, 2)

# Função para gerar renda anual baseada na renda mensal
def gerar_renda_anual(renda_mensal):
    # Adicionar variação para representar bônus, 13º, etc.
    multiplicador = random.uniform(11.5, 14)
    return round(renda_mensal * multiplicador, 2)

# Função para gerar score de crédito baseado em vários fatores
def gerar_score_credito(idade, renda_mensal, tempo_emprego, inadimplencia):
    base = random.randint(300, 700)
    
    # Fatores que aumentam o score
    if idade > 30:
        base += random.randint(0, 50)
    if renda_mensal > 5000:
        base += random.randint(0, 100)
    if tempo_emprego > 5:
        base += random.randint(0, 100)
    
    # Fatores que diminuem o score
    if inadimplencia:
        base -= random.randint(50, 200)
    
    # Garantir que o score esteja entre 0 e 1000
    return max(0, min(1000, base))

# Função para determinar aprovação de crédito e valor aprovado
def aprovar_credito(score, renda_mensal, valor_solicitado, outros_emprestimos, valor_outros_emprestimos):
    # Capacidade de pagamento (30% da renda mensal)
    capacidade_pagamento = renda_mensal * 0.3
    
    # Comprometimento atual com outros empréstimos
    comprometimento = 0
    if outros_emprestimos:
        comprometimento = valor_outros_emprestimos / 12  # Estimativa mensal
    
    # Capacidade disponível
    disponivel = max(0, capacidade_pagamento - comprometimento)
    
    # Valor máximo baseado no score
    fator_score = score / 1000  # Normalizado entre 0 e 1
    valor_maximo_score = valor_solicitado * fator_score * 1.5
    
    # Valor máximo baseado na capacidade de pagamento (considerando prazo médio de 24 meses)
    valor_maximo_capacidade = disponivel * 24
    
    # Valor aprovado é o menor entre os dois
    valor_aprovado = min(valor_maximo_score, valor_maximo_capacidade, valor_solicitado)
    
    # Critérios de aprovação
    aprovado = (
        score >= 500 and 
        disponivel > 0 and 
        valor_aprovado >= valor_solicitado * 0.5
    )
    
    if not aprovado:
        valor_aprovado = 0
    
    return aprovado, round(valor_aprovado, 2)

# Gerar o dataset
def gerar_dataset(num_registros=1000):
    dados = []
    
    for _ in range(num_registros):
        # Gerar dados básicos
        nome = gerar_nome()
        trabalho = random.choices(ocupacoes, weights=pesos_ocupacoes)[0]
        data_nascimento, idade = gerar_data_nascimento()
        
        # Gerar dados financeiros
        tempo_emprego = min(idade - 18, random.uniform(0, 40)) if idade > 18 else 0
        renda_mensal = gerar_renda_mensal(trabalho, idade)
        renda_anual = gerar_renda_anual(renda_mensal)
        
        # Gerar dados de crédito
        possui_inadimplencia = random.random() < 0.2  # 20% de chance de ter inadimplência
        score_credito = gerar_score_credito(idade, renda_mensal, tempo_emprego, possui_inadimplencia)
        
        possui_outros_emprestimos = random.random() < 0.3  # 30% de chance de ter outros empréstimos
        valor_outros_emprestimos = 0
        if possui_outros_emprestimos:
            valor_outros_emprestimos = random.uniform(1000, min(200000, renda_anual * 0.8))
        
        valor_solicitado = random.uniform(500, min(100000, renda_anual * 0.5))
        prazo_pagamento = random.choice([6, 12, 18, 24, 36, 48, 60])
        
        # Determinar aprovação e valor
        aprovado, valor_aprovado = aprovar_credito(
            score_credito, 
            renda_mensal, 
            valor_solicitado, 
            possui_outros_emprestimos, 
            valor_outros_emprestimos
        )
        
        # Adicionar ao dataset
        dados.append({
            'nome': nome,
            'trabalho': trabalho,
            'renda_mensal': renda_mensal,
            'renda_anual': renda_anual,
            'data_nascimento': data_nascimento,
            'idade': idade,
            'score_credito': score_credito,
            'possui_historico_inadimplencia': 'Sim' if possui_inadimplencia else 'Não',
            'tempo_emprego_atual': round(tempo_emprego, 1),
            'valor_solicitado': valor_solicitado,
            'prazo_pagamento': prazo_pagamento,
            'possui_outros_emprestimos': 'Sim' if possui_outros_emprestimos else 'Não',
            'valor_outros_emprestimos': valor_outros_emprestimos,
            'credito_aprovado': 'Sim' if aprovado else 'Não',
            'valor_aprovado': valor_aprovado
        })
    
    return pd.DataFrame(dados)

# Gerar dataset com 1000 registros
try:
    dataset = gerar_dataset(1000)
    
    # Salvar o dataset em formato CSV
    dataset.to_csv('dataset_aprovacao_credito.csv', index=False)
    
    # Exibir informações sobre o dataset
    print(f"Dataset gerado com sucesso! Total de registros: {len(dataset)}")
    print(f"Taxa de aprovação: {dataset['credito_aprovado'].value_counts(normalize=True)['Sim']*100:.2f}%")
    print("\nPrimeiros 5 registros:")
    print(dataset.head())
    
    # Estatísticas básicas
    print("\nEstatísticas básicas:")
    print(dataset[['renda_mensal', 'renda_anual', 'idade', 'score_credito', 'valor_solicitado', 'valor_aprovado']].describe())
    
except Exception as e:
    print(f"Erro ao gerar dataset: {e}")
