# AquaGuard — Sistema Inteligente de Monitoramento e Prevenção de Enchentes

integrantes:

Ícaro Henrique de Souza Calixto RM560278                                                                                                                                 
Caio Costa Beraldo RM560775        
Henrique Celso Moura da Paixão Filho RM559687                            
Victor Kenzo Mikado RM560057

Classificação de risco de enchentes com Python e Random Forest.

## Arquivos
- `AquaGuard_Machine_Learning_Enchentes.ipynb`: notebook principal.
- `api_exemplo.py`: exemplo opcional de API com FastAPI.
- `requirements.txt`: dependências para execução local.

## Como executar
1. Abra [https://colab.research.google.com/](https://colab.research.google.com/drive/1Q20XWkJvjkjz2zqdFkL7Gig4GlvSt490?usp=sharing)
2. Faça upload de `AquaGuard_Machine_Learning_Enchentes.ipynb`.
3. Selecione **Ambiente de execução > Executar tudo**.
4. Aguarde todas as células e salve/baixe o notebook com as saídas.

## Variáveis de entrada
Chuva acumulada em 24 horas, nível do rio, saturação do solo, capacidade de drenagem e altitude.

## Modelo
Random Forest Classifier, com divisão treino/teste estratificada de 80%/20%. A avaliação apresenta acurácia, F1-score macro, relatório de classificação, matriz de confusão e importância das variáveis.

## Limitação importante
O notebook gera 2.500 registros sintéticos. Os rótulos são construídos por uma regra didática. Portanto, as métricas medem a reprodução dessa regra simulada, não a capacidade comprovada de prever enchentes reais. Para aplicação real, são necessários dados históricos e sensores confiáveis, validação externa e acompanhamento especializado.
