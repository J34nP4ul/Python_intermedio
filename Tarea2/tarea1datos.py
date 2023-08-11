import requests as req
import os

def obtenerDatos(pais):
    url = f"https://disease.sh/v3/covid-19/countries/{pais}"
    response = req.get(url)
    data = response.json()
    return data

def mostrarDatos(datosPais, opcion):
    opciones = {
        "casos": "cases",
        "muertes": "deaths",
        "recuperaciones": "recovered"
    }

    contenido = f"\nDatos COVID-19 en {datosPais['country']}:\n"
    contenido += f"- {opcion.capitalize()} totales: {datosPais[opciones[opcion]]}\n"

    return contenido

def main():
    url_base = "https://disease.sh/v3/covid-19"

    while True:
        print("Bienvendido al programa que muestra las cifras COVID-19 en Centroamerica")
        print("Paises disponibles: Guatemala, El Salvador, Honduras, Nicaragua, Costa Rica, Panama")
        print("para terminar el programa puede escribir la palabra 'salir'")
        paisesInput = input("Ingrese los nombres de los países separados por comas (por ejemplo, 'Guatemala, El Salvador'): ")

        if paisesInput.lower() == "salir":
            print("Gracias por utilizar nuestros servicios. Hasta Luego!!!")
            break

        
        opciones_validas = {"casos", "muertes", "recuperaciones"}
        opcion = ""
        while opcion not in opciones_validas:
            opcion = input("Seleccione la opción que desea saber (casos, muertes, recuperaciones): ").lower()

        
if __name__ == "__main__":
    main()
