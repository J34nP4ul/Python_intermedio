import requests as req
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def obtenerDatos(pais):
    url = f"https://disease.sh/v3/covid-19/countries/{pais}" #url de donde se tomaran los datos
    response = req.get(url)
    data = response.json()
    return data

def main():
    paises = ["Guatemala", "El Salvador", "Honduras", "Nicaragua", "Costa Rica", "Panama"]
    opcionesValidas = ["casos", "muertes", "recuperaciones", "todos"]
    #paises y datos seleccionados de todos los que existen en la pagina
    #pueden incluirse mas datos y mas paises de se necesarios
    matrizDatos = []

    for opcion in opcionesValidas[:-1]:
        contenidOpcion = mostrarDatos(opcion, paises)
        matrizDatos.extend(contenidOpcion)
        
    matNumpy = np.array(matrizDatos) #crearemos una matriz para el mejor manejo de los datos
    columnas = ["País", "Opción", "Dato"]
    defMat = pd.DataFrame(matNumpy, columns=columnas)

    while True:
        print ("\nBienvenido al programa que te muestra los datos mas relevntes de COVID-19 en Centroamerica\n")
        opcion = input("Elija qué gráfica desea ver (casos, muertes, recuperaciones, todos) o escriba 'salir': ")
        if opcion.lower() == "salir": #menu de selecciones multiples
            break
        elif opcion.lower() in opcionesValidas:
            if opcion.lower() == "todos":
                graficarTodos(defMat)
            else:
                graficarDatos(defMat, opcion.lower()) 
        else:
            print("Opción inválida. Por favor, elija una opción válida o escriba 'salir'.")

def mostrarDatos(opcion, datosPaises):
    opciones = {
        "casos": "cases",
        "muertes": "deaths",    #estas son las opciones que hemos elegido de la pagina para graficar
        "recuperaciones": "recovered"
    }

    contenido = []
    for pais in datosPaises:
        datosPais = obtenerDatos(pais) #aqui halamos de la pagina los paises que queremos mostrar
        contenidoPais = [pais, opcion.capitalize(), str(datosPais[opciones[opcion]])]
        contenido.append(contenidoPais)
    
    return contenido

def graficarDatos(df, opcion):
    df_opcion = df[df["Opción"] == opcion.capitalize()].copy()
    df_opcion["Dato"] = df_opcion["Dato"].astype(int)
    
    plt.figure(figsize=(10, 6))
    plt.bar(df_opcion["País"], df_opcion["Dato"], color='skyblue')
    plt.title(f"Grafico de {opcion.capitalize()} por País")
    plt.xlabel("País")          #utilizamos el modulo de matplotlilb para graficar los datos
    plt.ylabel(opcion.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    
        # Formatear el eje Y para mostrar números legibles
    plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))

    plt.show()

def graficarTodos(df):
    df_casos = df[df["Opción"] == "Casos"].copy()
    df_casos["Dato"] = df_casos["Dato"].astype(int)
                                                        #creamos un grafico general de todos los datos
    df_muertes = df[df["Opción"] == "Muertes"].copy()
    df_muertes["Dato"] = df_muertes["Dato"].astype(int)
    
    df_recuperaciones = df[df["Opción"] == "Recuperaciones"].copy()
    df_recuperaciones["Dato"] = df_recuperaciones["Dato"].astype(int)

    plt.figure(figsize=(12, 8))
    plt.bar(df_casos["País"], df_casos["Dato"], color='green', label='Casos')
    plt.bar(df_muertes["País"], df_muertes["Dato"], color='red', label='Muertes')
    plt.bar(df_recuperaciones["País"], df_recuperaciones["Dato"], color='blue', label='Recuperaciones')
    plt.title("Grafico de Casos, Muertes y Recuperaciones por País")
    plt.xlabel("País")
    plt.ylabel("Cantidad")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    
        # Formatear el eje Y para mostrar números legibles
    plt.gca().yaxis.set_major_formatter(plt.ScalarFormatter(useMathText=True))

    plt.show()

if __name__ == "__main__":
    main()