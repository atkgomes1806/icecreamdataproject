---
updated_date: 2025-03-14
created_date: 2025-03-14
---
# 1 Projeto 1 -  **Previsão de Vendas do Sorvete Gelato Mágico – Um Modelo de Machine Learning Aplicado**

## 1.1 Sumário
- [ ] [[#1.2 **Contexto e História do Caso de Uso**]]
- [ ] [[#1.3 **Desafio e Solução**]]
- [ ] [[#1.4 Dataset]]
- [ ] [[# Prepara o ambiente no Azure Machine Learning]]
- [ ] Carregar e explorar os dados de vendas de Sorvetes
- [ ] Treinar um modelo de Regressão
- [ ] Registrar o modelo e os experimentos usando MLFlow
- [ ] Implantar o modelo para fazer previsões em tempo real

## 1.2 **Contexto e História do Caso de Uso**
A **Gelato Mágico** é uma sorveteria localizada em **Recife, Pernambuco**, uma cidade conhecida pelo seu clima quente e úmido. Com um grande volume de clientes, a sorveteria percebeu um padrão importante: as vendas de sorvetes variam conforme a temperatura ambiente.

O proprietário, João, enfrentava um desafio recorrente: **como otimizar a produção para evitar desperdícios e garantir estoque suficiente para atender à demanda?** A superprodução gerava prejuízos com desperdício, enquanto a produção insuficiente resultava em clientes insatisfeitos e perda de vendas.

## 1.3 **Desafio e Solução**
Para resolver esse problema, foi desenvolvido um modelo de **Machine Learning** capaz de prever a quantidade de sorvetes que serão vendidos com base na temperatura do dia. Com essa previsão, a Gelato Mágico pode planejar sua produção de forma estratégica, reduzindo desperdício e garantindo que todos os clientes sejam atendidos.

O projeto aplica conceitos de aprendizado de máquina, análise exploratória de dados e modelagem preditiva para otimizar a tomada de decisão na sorveteria. Como resultado, a empresa melhora sua eficiência operacional e aprimora a experiência dos clientes.

### 1.3.1 **Impacto e Relevância**
A utilização de **Machine Learning no setor alimentício** demonstra como a tecnologia pode ser aplicada a desafios reais, trazendo soluções inovadoras para o mercado. Esse projeto reforça a importância da análise de dados para a otimização de processos e mostra como a inteligência artificial pode ser um diferencial competitivo.

## 1.4 **Objetivo**
O objetivo deste projeto é desenvolver um **modelo de regressão preditiva** para:

✅ **Treinar um modelo de Machine Learning** para prever as vendas de sorvete com base na temperatura.
✅ **Registrar e gerenciar o modelo** usando MLflow.
✅ **Implementar o modelo para previsões em tempo real** em um ambiente de cloud computing.
✅ **Criar um pipeline estruturado** para garantir a reprodutibilidade do modelo.

## 1.5 Dataset
O dataset utilizado contém dados sobre as vendas diárias de sorvete (em unidades), datas (YYYY-MM-DD) e a temperatura do dia (em ºC). O dataset possui 100 registros, baseados nas temperaturas reais da cidade do Recife.

## 1.6 Prepara o ambiente no Azure Machine Learning
- [ ] Criar um Resource Group: rg-gelato
	- [ ] Nome: rg-gelato

### 1.6.1 Criar o Machine Learning Workspace
### 1.6.2 Criar uma VM (Instância)
- Obs:
  - Escolha uma opção econômica.

### 1.6.3 Criar um Cluster

### 1.6.4 Upload do Dataset
- Carregar o arquivo CSV gerado.
- Utilizar o local file.
- Remover a coluna Data para análise.

## 1.7 Treinar um modelo de Regressão
### 1.7.1 Criar um AutoML do Modelo
- Nome do experimento: experimento-automl
- TaskType: Regressão
- Coluna alvo: Vendas de sorvete
- Configurações:
  - Max nodes: 2
  - Experiment timeout: 15 min
  - Iteration timeout: 15 min
- Task settings:
  - Bloquear todos os modelos exceto XGBoostRegressor.

## 1.8 Criar um Designer
- Alternativa para treinar os modelos manualmente.
### 1.8.1 Selecione o dataset e arraste para o flow
### 1.8.2 Criar o fluxo no Designer
#### 1.8.2.1 Configurar e Submeter o fluxo

## 1.9 Parabéns! Projeto Concluído.

