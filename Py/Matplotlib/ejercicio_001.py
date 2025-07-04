import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

fig = plt.figure()
# plot 1
ax = fig.add_subplot(2, 2, 1)
ax.set_title(f'Subplot 1')
ax.set_xlabel('Etiqueta para el eje X')
ax.set_ylabel('Etiqueta para el eje Y')
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
ax.yaxis.grid(which='minor', linestyle='dashed', color='lightskyblue')
# plot 2
ax = fig.add_subplot(2, 2, 2)
ax.set_title(f'Subplot 2')
ax.set_xlabel('Etiqueta para el eje X')
ax.set_ylabel('Etiqueta para el eje Y')
ax.xaxis.set_minor_locator(MultipleLocator(0.1))
ax.xaxis.grid(which='minor', linestyle='dashed', color='gray')
ax.xaxis.grid(color='r', linestyle='-')
# plot 3
ax = fig.add_subplot(2, 2, 3)
ax.set_title(f'Subplot 3')
ax.set_xlabel('Etiqueta para el eje X')
ax.set_ylabel('Etiqueta para el eje Y')
ax.yaxis.set_minor_locator(MultipleLocator(0.05))
ax.yaxis.grid(which='minor', linestyle='dashed', color='lightskyblue')
# plot 4
ax = fig.add_subplot(2, 2, 4)
ax.set_title(f'Subplot 4')
ax.set_xlabel('Etiqueta para el eje X')
ax.set_ylabel('Etiqueta para el eje Y')
ax.xaxis.grid(color='r', linestyle='-')
ax.yaxis.grid(color='b', linestyle='-')
# espacio entre marcos
fig.tight_layout(pad=1.5)
