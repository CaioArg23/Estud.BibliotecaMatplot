#para mostrar apenas os pontos de uma intersecção basta utilizar a conotação 'o'. Ex:
import matplotlib.pyplot as plt 
import numpy as np 

eixoX = np.array([1, 2, 4, 12, 30])
eixoY = np.array([2, 4, 7, 20, 31])

plt.plot (eixoX, eixoY, marker = 'D')
plt.show()