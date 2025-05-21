from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)
# Carregar modelos e encoders
clf = joblib.load('modelo_credito_classificacao.joblib')
reg = joblib.load('modelo_credito_regressao.joblib')
le_dict = joblib.load('encoders.joblib')

@app.route('/classificar', methods=['POST'])
def classificar():
    data = request.json
    df_novo = pd.DataFrame([data])

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
        limite = reg.predict(df_novo)[0]
        return jsonify({
            "aprovado": True,
            "limite": round(float(limite), 2)
        })
    else:
        return jsonify({
            "aprovado": False,
            "limite": 0.0
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')