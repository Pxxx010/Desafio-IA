import pandas as pd
import joblib

# Carregar modelos e encoders
clf = joblib.load('modelo_credito_classificacao.joblib')
reg = joblib.load('modelo_credito_regressao.joblib')
le_dict = joblib.load('encoders.joblib')

# Exemplo de novo dado (edite conforme necessário)
novo_dado = {
    'trabalho': 'Desempregado',
    'renda_mensal': 800,
    'renda_anual': 9600,
    'idade': 45,
    'score_credito': 300,
    'possui_historico_inadimplencia': 'Sim',
    'tempo_emprego_atual': 0,
    'valor_solicitado': 10000,
    'prazo_pagamento': 48,
    'possui_outros_emprestimos': 'Sim',
    'valor_outros_emprestimos': 1500.0
}

# Transformar em DataFrame
df_novo = pd.DataFrame([novo_dado])

# Aplicar os encoders
for col, le in le_dict.items():
    if col in df_novo:
        df_novo[col] = le.transform(df_novo[col])

# Garantir que as colunas estejam na mesma ordem do treino
colunas_usadas = clf.feature_names_in_
df_novo = df_novo[colunas_usadas]

# Fazer a predição de aprovação
pred = clf.predict(df_novo)[0]

if pred == 1:
    # Se aprovado, prever o limite sugerido
    limite = reg.predict(df_novo)[0]
    print("Crédito aprovado!")
    print(f"Limite sugerido para o cliente: R$ {limite:.2f}")
else:
    print("Crédito NÃO aprovado para o cliente.")