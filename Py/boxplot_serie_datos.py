import matplotlib.pyplot as plt
import seaborn as sns

# Datos
datos = [6, 8, 9, 10, 12]

# Estilo
sns.set(style="whitegrid")

# Crear boxplot
plt.figure(figsize=(6, 4))
sns.boxplot(data=datos, orient="h", color="skyblue")

# Título y ejes
plt.title("Boxplot de los datos")
plt.xlabel("Valores")

# Mostrar
plt.show()
