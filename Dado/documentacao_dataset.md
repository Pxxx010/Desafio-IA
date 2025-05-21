# Documentação do Dataset para Sistema de Aprovação de Crédito

## Visão Geral

Este dataset foi criado para servir como base para o desenvolvimento de um sistema de aprovação de crédito utilizando técnicas de Inteligência Artificial. O dataset contém 1000 registros sintéticos que simulam clientes solicitando crédito, com informações pessoais, financeiras e o resultado da análise de crédito.

## Estrutura do Dataset

O dataset contém as seguintes variáveis:

### Variáveis Solicitadas
1. **nome** - Nome completo do cliente (texto)
2. **trabalho** - Ocupação profissional (categórica)
3. **renda_mensal** - Renda mensal bruta em Reais (numérica)
4. **renda_anual** - Renda anual bruta em Reais (numérica)
5. **data_nascimento** - Data de nascimento no formato DD/MM/AAAA (data)

### Variáveis Adicionais
6. **idade** - Idade calculada a partir da data de nascimento (numérica)
7. **score_credito** - Pontuação de crédito do cliente, de 0 a 1000 (numérica)
8. **possui_historico_inadimplencia** - Indica se o cliente tem histórico de inadimplência (Sim/Não)
9. **tempo_emprego_atual** - Tempo no emprego atual em anos (numérica)
10. **valor_solicitado** - Valor do crédito solicitado em Reais (numérica)
11. **prazo_pagamento** - Prazo para pagamento do crédito em meses (numérica)
12. **possui_outros_emprestimos** - Indica se o cliente possui outros empréstimos ativos (Sim/Não)
13. **valor_outros_emprestimos** - Valor total de outros empréstimos em Reais (numérica)

### Variáveis Alvo (Target)
14. **credito_aprovado** - Indica se o crédito foi aprovado (Sim/Não)
15. **valor_aprovado** - Valor do crédito aprovado em Reais (numérica)

## Estatísticas do Dataset

### Informações Gerais
- **Total de registros**: 1000
- **Taxa de aprovação de crédito**: 49,40%
- **Valores ausentes**: 0
- **Inconsistências**: 0

### Distribuição das Variáveis Categóricas

#### Distribuição por Tipo de Trabalho
- Funcionário de Empresa Privada: 35,0%
- Funcionário Público: 16,4%
- Empresário/Autônomo: 15,8%
- Aposentado/Pensionista: 11,3%
- Profissional Liberal: 9,4%
- Estudante: 5,3%
- Desempregado: 4,3%
- Outros: 2,5%

#### Distribuição por Histórico de Inadimplência
- Sem histórico de inadimplência: 79,3%
- Com histórico de inadimplência: 20,7%

#### Distribuição por Outros Empréstimos
- Sem outros empréstimos: 70,5%
- Com outros empréstimos: 29,5%

### Estatísticas das Variáveis Numéricas

| Variável | Média | Desvio Padrão | Mínimo | Mediana | Máximo |
|----------|-------|---------------|--------|---------|--------|
| Renda Mensal | R$ 9.751,62 | R$ 8.211,98 | R$ 8,14 | R$ 7.712,44 | R$ 50.554,64 |
| Renda Anual | R$ 124.146,95 | R$ 104.780,62 | R$ 105,25 | R$ 96.829,74 | R$ 656.976,13 |
| Idade | 49,5 | 17,5 | 18 | 50 | 80 |
| Score de Crédito | 551,7 | 177,9 | 100 | 550 | 950 |
| Tempo de Emprego | 10,7 | 9,5 | 0 | 8,2 | 40,0 |
| Valor Solicitado | R$ 27.028,00 | R$ 24.110,85 | R$ 309,13 | R$ 20.741,28 | R$ 99.844,88 |
| Valor Aprovado | R$ 13.916,61 | R$ 21.917,47 | R$ 0,00 | R$ 0,00 | R$ 99.844,88 |

## Correlações Importantes

As principais correlações observadas no dataset são:

1. **Renda Mensal e Valor Solicitado**: 0,60 - Clientes com maior renda tendem a solicitar valores maiores
2. **Score de Crédito e Valor Aprovado**: 0,44 - Score de crédito tem forte influência na aprovação
3. **Renda Mensal e Valor Aprovado**: 0,40 - Renda é um fator importante na aprovação
4. **Idade e Renda Mensal**: 0,30 - Clientes mais velhos tendem a ter rendas maiores

## Uso Recomendado para IA

Este dataset é adequado para os seguintes tipos de modelos de IA:

1. **Classificação Binária**: Prever se um crédito será aprovado ou não
2. **Regressão**: Prever o valor que será aprovado para um cliente
3. **Análise de Risco**: Identificar fatores de risco para inadimplência
4. **Segmentação de Clientes**: Agrupar clientes com perfis similares

## Arquivos Disponíveis

1. **dataset_aprovacao_credito.csv**: Dataset principal com todos os registros
2. **estrutura_dataset.md**: Documentação detalhada da estrutura do dataset
3. **visualizacoes/**: Diretório com gráficos e análises estatísticas
4. **gerar_dataset.py**: Script Python usado para gerar o dataset
5. **validar_dataset.py**: Script Python usado para validar o dataset

## Observações Finais

Este dataset foi gerado sinteticamente e não contém dados reais de clientes. As relações entre as variáveis foram criadas para simular um cenário realista de aprovação de crédito, considerando fatores como renda, score de crédito, histórico de inadimplência e capacidade de pagamento.

O algoritmo de aprovação de crédito considera principalmente:
- Score de crédito (mínimo de 500 pontos)
- Capacidade de pagamento (30% da renda mensal)
- Comprometimento com outros empréstimos
- Valor solicitado em relação à capacidade financeira

Este dataset pode ser expandido com mais registros ou variáveis adicionais conforme necessário para o desenvolvimento do sistema de IA.
