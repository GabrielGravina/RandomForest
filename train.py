from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from DecisionTree import DecisionTree

# Carrega dados
data = datasets.load_breast_cancer()
X, y = data.data, data.target

# Divide dados
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

# Treina modelo
clf = DecisionTree(max_depth=10)
clf.fit(X_train, y_train)

# Faz previsões
predictions = clf.predict(X_test)

# Avalia acurácia
def accuracy(y_test, y_pred):
    return np.sum(y_test == y_pred) / len(y_test)

acc = accuracy(y_test, predictions)
print(f"Acurácia: {acc:.2f}")

# === VISUALIZAÇÃO ===
# 1. Gera visualização gráfica (Graphviz)
dot = clf.export_graphviz(
    feature_names=data.feature_names,
    class_names=data.target_names
)
dot.render("decision_tree", format="png", cleanup=True)
dot.view()  # Abre a imagem automaticamente

# 2. Visualização em texto (opcional)
print("\n=== Árvore em Texto ===")
clf.visualize()