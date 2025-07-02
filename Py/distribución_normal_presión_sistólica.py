import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Distribución normal con media 120, desviación 10
x = np.linspace(80, 160, 500)
y = norm.pdf(x, loc=120, scale=10)

plt.plot(x, y, label="N(120, 10²)")
plt.fill_between(x, y, alpha=0.3)
plt.title("Distribución Normal de presión sistólica")
plt.xlabel("mmHg")
plt.ylabel("Densidad de probabilidad")
plt.grid()
plt.legend()
plt.show()
