import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, mean_absolute_error, accuracy_score
import joblib
import warnings
warnings.filterwarnings('ignore')

# Carregar o dataset
# Fonte dos dados: (adicione o link da base aqui)
df = pd.read_csv('dataset_aprovacao_credito.csv')

# Remover colunas que não serão usadas
df = df.drop(['nome', 'data_nascimento'], axis=1)

# 3. Verificar e tratar valores faltantes
print('Valores faltantes por coluna:')
print(df.isnull().sum())
# Se houver valores faltantes, preencher com a mediana (numérico) ou moda (categórico)
for col in df.columns:
    if df[col].isnull().sum() > 0:
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
print('Valores faltantes tratados!')

# Transformar colunas categóricas em números
le_dict = {}
for col in df.select_dtypes(include='object').columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    le_dict[col] = le

# Separar features e target para classificação
X = df.drop(['credito_aprovado', 'valor_aprovado'], axis=1)
y = df['credito_aprovado']

# Separar em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Treinar e avaliar pelo menos dois modelos diferentes
# Modelo 1: RandomForest
clf_rf = RandomForestClassifier(random_state=42)
clf_rf.fit(X_train, y_train)
y_pred_rf = clf_rf.predict(X_test)
acc_rf = accuracy_score(y_test, y_pred_rf)
print('\nRandomForestClassifier:')
print(classification_report(y_test, y_pred_rf))
print(f'Acurácia: {acc_rf:.4f}')

# Modelo 2: LogisticRegression
clf_lr = LogisticRegression(max_iter=1000, random_state=42)
clf_lr.fit(X_train, y_train)
y_pred_lr = clf_lr.predict(X_test)
acc_lr = accuracy_score(y_test, y_pred_lr)
print('\nLogisticRegression:')
print(classification_report(y_test, y_pred_lr))
print(f'Acurácia: {acc_lr:.4f}')

# 5. Escolher o melhor modelo com base na acurácia
if acc_rf >= acc_lr:
    melhor_modelo = clf_rf
    nome_modelo = 'RandomForestClassifier'
    melhor_acc = acc_rf
else:
    melhor_modelo = clf_lr
    nome_modelo = 'LogisticRegression'
    melhor_acc = acc_lr
print(f'\nMelhor modelo escolhido: {nome_modelo} (Acurácia: {melhor_acc:.4f})')

# Agora, treinar o modelo de regressão apenas para os aprovados
df_aprovados = df[df['credito_aprovado'] == 1]
X_reg = df_aprovados.drop(['credito_aprovado', 'valor_aprovado'], axis=1)
y_reg = df_aprovados['valor_aprovado']

X_reg_train, X_reg_test, y_reg_train, y_reg_test = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)
reg = RandomForestRegressor(random_state=42)
reg.fit(X_reg_train, y_reg_train)

# Avaliar regressão
y_reg_pred = reg.predict(X_reg_test)
print('Erro médio absoluto do limite sugerido:', mean_absolute_error(y_reg_test, y_reg_pred))

# Salvar melhor modelo e encoders
joblib.dump(melhor_modelo, 'modelo_credito_classificacao.joblib')
joblib.dump(reg, 'modelo_credito_regressao.joblib')
joblib.dump(le_dict, 'encoders.joblib')
print('Modelos e encoders salvos!')