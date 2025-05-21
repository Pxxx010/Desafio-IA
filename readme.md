# Simulador de Aprovação de Crédito

Este projeto consiste em uma API de classificação de crédito e um frontend web para simulação de aprovação e sugestão de limite de crédito.

## Estrutura

- **api/**: Contém a API Flask, modelos treinados, dataset e scripts de treinamento.
- **frontend/**: Contém o frontend web (HTML + JS) para interação com a API.
- **Dado/**: Contém scripts e documentação para geração e validação do dataset.

---

## Como rodar a API

1. **Acesse a pasta da API:**

   ```bash
   cd api
   ```
2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```
3. **(Opcional) Treine o modelo:**

   - Se quiser treinar novamente, execute:
     ```bash
     python treinar_modelo.py
     ```
4. **Inicie a API:**

   ```bash
   python api_credito.py
   ```

   - A API estará disponível em `http://localhost:5000` (ou `http://<seu_ip_local>:5000` para acesso em rede).

---

## Como rodar o Frontend

1. **Acesse a pasta do frontend:**

   ```bash
   cd frontend
   ```
2. **Abra o arquivo `frontend_credito.html` no navegador.**

   - Dê dois cliques ou use `Ctrl+O` no navegador e selecione o arquivo.
3. **Preencha o formulário e clique em \"Classificar\".**

   - O frontend irá se comunicar com a API e mostrar o resultado.

---

## Observações

- Certifique-se de que a API está rodando antes de usar o frontend.
- Se for acessar de outro computador/dispositivo, altere a URL da API no JavaScript do frontend para o IP da máquina onde a API está rodando (ex: `http://192.168.0.10:5000/classificar`).
- Se necessário, libere a porta 5000 no firewall.

---

## Dependências

- Python 3.8+
- Flask
- Flask-CORS
- pandas
- scikit-learn
- joblib

---

## Fonte dos Dados

- Os dados foram gerados via Python, usando os scripts da pasta `Dado/`:
  - `gerar_dataset.py`: Script para gerar o dataset de simulação.
  - `validar_dataset.py`: Script para validar a integridade dos dados.
  - `documentacao_dataset.md`: Documentação detalhada do dataset.
  - `estrutura_dataset.md`: Descrição da estrutura e variáveis do dataset.

---

## Licença

Este projeto é livre para fins acadêmicos e de estudo.
