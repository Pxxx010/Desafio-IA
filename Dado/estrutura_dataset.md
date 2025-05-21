# Estrutura do Dataset para Sistema de Aprovação de Crédito

## Variáveis do Dataset

1. **nome** - Nome completo do cliente
   - Tipo: String
   - Descrição: Nome e sobrenome do solicitante de crédito

2. **trabalho** - Ocupação profissional
   - Tipo: String (Categórica)
   - Categorias principais:
     - Funcionário Público
     - Funcionário de Empresa Privada
     - Empresário/Autônomo
     - Aposentado/Pensionista
     - Profissional Liberal
     - Desempregado
     - Estudante
     - Outros

3. **renda_mensal** - Renda mensal bruta
   - Tipo: Numérico (Float)
   - Unidade: Reais (R$)
   - Faixa: R$ 0,00 a R$ 50.000,00

4. **renda_anual** - Renda anual bruta
   - Tipo: Numérico (Float)
   - Unidade: Reais (R$)
   - Faixa: R$ 0,00 a R$ 600.000,00
   - Observação: Em geral, será aproximadamente 12x a renda mensal, com possíveis variações para bonificações e rendas sazonais

5. **data_nascimento** - Data de nascimento
   - Tipo: Data (String formatada)
   - Formato: DD/MM/AAAA
   - Faixa: Considerando pessoas entre 18 e 80 anos

6. **idade** - Idade calculada a partir da data de nascimento
   - Tipo: Numérico (Inteiro)
   - Faixa: 18 a 80 anos

## Variáveis Adicionais para Enriquecer o Dataset

7. **score_credito** - Pontuação de crédito do cliente
   - Tipo: Numérico (Inteiro)
   - Faixa: 0 a 1000
   - Descrição: Representa o histórico de crédito do cliente

8. **possui_historico_inadimplencia** - Indica se o cliente tem histórico de inadimplência
   - Tipo: Booleano (Sim/Não)

9. **tempo_emprego_atual** - Tempo no emprego atual
   - Tipo: Numérico (Float)
   - Unidade: Anos
   - Faixa: 0 a 40 anos

10. **valor_solicitado** - Valor do crédito solicitado
    - Tipo: Numérico (Float)
    - Unidade: Reais (R$)
    - Faixa: R$ 500,00 a R$ 100.000,00

11. **prazo_pagamento** - Prazo para pagamento do crédito
    - Tipo: Numérico (Inteiro)
    - Unidade: Meses
    - Faixa: 6 a 60 meses

12. **possui_outros_emprestimos** - Indica se o cliente possui outros empréstimos ativos
    - Tipo: Booleano (Sim/Não)

13. **valor_outros_emprestimos** - Valor total de outros empréstimos
    - Tipo: Numérico (Float)
    - Unidade: Reais (R$)
    - Faixa: R$ 0,00 a R$ 200.000,00

## Variável Alvo (Target)

14. **credito_aprovado** - Indica se o crédito foi aprovado
    - Tipo: Booleano (Sim/Não)

15. **valor_aprovado** - Valor do crédito aprovado
    - Tipo: Numérico (Float)
    - Unidade: Reais (R$)
    - Faixa: R$ 0,00 (não aprovado) a R$ 100.000,00
    - Observação: Pode ser menor que o valor solicitado, dependendo da análise de crédito
