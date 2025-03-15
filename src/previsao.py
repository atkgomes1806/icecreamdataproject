import joblib
import numpy as np

def prever_vendas(temperatura):
    # Carregar o modelo treinado
    modelo = joblib.load('modelo_sorvete.pkl')
    
    # Fazer a previsão
    previsao = modelo.predict(np.array([[temperatura]]))
    return previsao[0]

if __name__ == "__main__":
    temp = float(input("Digite a temperatura atual: "))
    vendas_previstas = prever_vendas(temp)
    print(f'Previsão de vendas: {vendas_previstas:.0f} sorvetes')
