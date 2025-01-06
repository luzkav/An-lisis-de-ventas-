
# Análisis básico de ventas
# Autor: Karime

# Importar las librerías necesarias
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos ficticios de ventas
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
    "Ventas": [1500, 2300, 1800, 2000, 3000, 2500]
}
df = pd.DataFrame(data)

# Mostrar los primeros registros
print("Datos de ventas:")
print(df)

# Calcular estadísticas básicas
total_ventas = df["Ventas"].sum()
promedio_ventas = df["Ventas"].mean()

print(f"Total de ventas: {total_ventas}")
print(f"Promedio de ventas: {promedio_ventas:.2f}")

# Crear un gráfico de barras
plt.bar(df["Mes"], df["Ventas"], color="skyblue")
plt.title("Ventas mensuales")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.tight_layout()
plt.savefig("ventas_mensuales.png")
plt.show()
