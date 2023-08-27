import matplotlib.pyplot as plt
import numpy as np

# Gerar dados aleatórios para o exemplo
dados = np.random.normal(0, 1, 1000)  # Dados normalmente distribuídos

# Plotar o histograma
plt.hist(dados, bins=20, color='blue', edgecolor='black')
plt.title("Histograma de Dados Aleatórios")
plt.xlabel("Valor")
plt.ylabel("Frequência")
plt.show()
