# 📌 Previsão de Vendas de Sorvetes - Gelato Mágico

## 📖 Descrição do Projeto
Este projeto tem como objetivo desenvolver um modelo de Machine Learning para prever as vendas diárias de sorvetes da sorveteria **Gelato Mágico**, localizada em **Recife-PE**. A previsão será baseada na temperatura do dia, permitindo otimizar a produção, reduzir desperdícios e maximizar as vendas.

## 🚀 Tecnologias Utilizadas
- **Python** 🐍
- **Pandas** 📊
- **Scikit-Learn** 🤖
- **Azure Machine Learning** ☁️
- **MLflow** 📈

## 📂 Estrutura do Projeto
```
📂 icecreamdataproject
│── 📄 README.md          # Descrição do projeto
│── 📂 data               # Dados do projeto
│   ├── dataicecream.csv  # Dataset utilizado
│── 📂 src                # Código-fonte do projeto
│   ├── modelo.py         # Script para treinar o modelo
│   ├── previsao.py       # Script para realizar previsões
```

## 🎯 Objetivos
✅ Desenvolver um modelo de regressão preditiva para prever vendas de sorvetes com base na temperatura.  
✅ Registrar e gerenciar o modelo utilizando MLflow.  
✅ Implementar o modelo para previsões em tempo real usando Azure Machine Learning.  
✅ Criar um pipeline estruturado para treinar e testar o modelo.  

## 📊 Dataset
O dataset contém **100 registros** e inclui as seguintes colunas:
- `Data`: Data da venda (YYYY-MM-DD)
- `Vendas`: Número de sorvetes vendidos
- `Temperatura`: Temperatura registrada no dia (°C)

## 📌 Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/previsao-sorvetes.git
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o Jupyter Notebook para análise e treinamento do modelo:
   ```bash
   jupyter notebook
   ```
4. Para realizar previsões:
   ```bash
   python src/previsao.py
   ```

## 📈 Resultados Esperados
A aplicação de Machine Learning neste projeto permite prever com precisão a demanda diária por sorvetes, ajudando a sorveteria **Gelato Mágico** a ajustar sua produção e evitar desperdícios.

---
📌 **Desenvolvido por:** Arthur Gomes Soares 🚀
