import pandas as pd #modulo que puede leer archivos con datos
import matplotlib.pyplot as plt #modulo que puede crear graficos
ventas = pd.read_csv("ventas.csv")

ventas ["Ganancias"] = ventas["Ventas"] - ventas["Gastos"] #creando una nueva columna en el dataframe
print(ventas)

ventas.set_index("Mes", inplace=True)#con esta linea colocamos los meses en el eje de las x



plt.figure (figsize=(10,6))
plt.title("Ganancias por Mes")
plt.xlabel("Mes")               #creando el titulo y las leyendas de los ejes respectivos
plt.ylabel ("Ganancias")

plt.plot(ventas.index, ventas["Ganancias"], marker='o', linestyle='-', color='b', label='Ganancia')
plt.plot(ventas.index, ventas["Gastos"], marker='o', linestyle='-', color='r', label= 'Gastos' )
#creando las lineas de graficos con sus respectivos colores

plt.xticks(rotation=45)#crea la etiqueta en el eje de las X con una rotacion de 45°

plt.yticks(ventas["Ganancias"]) #crea los datos de el eje de las Y

plt.legend() #creando la leyenda

plt.tight_layout()
plt.show()
