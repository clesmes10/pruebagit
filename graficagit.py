import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, np.pi*2, 10000)
a = np.sin(x)
b= np.cos(x)
plt.plot(a, b)
plt.savefig("circulo.pdf")
plt.show()
