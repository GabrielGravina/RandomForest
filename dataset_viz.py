from sklearn.datasets import load_breast_cancer
import pandas as pd

# Carrega o dataset
data = load_breast_cancer()

# Cria DataFrame
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target  # Adiciona a coluna de classes

# Mostra informações
print("Primeiras 5 linhas:")
print(df.head())
print("\nDimensões:", df.shape)

# Exporta para Excel (substitui o CSV)
df.to_excel("breast_cancer.xlsx", index=False) 
print("\nDataset salvo como 'breast_cancer.xlsx'")