import requests as req


def chistesChuckNorris ():
    urlGet = "https://api.chucknorris.io/jokes/random"
    getResponse = req.get (urlGet)
    
    if getResponse.status_code == 200:
        data = getResponse.json()
        
        print ("respuesta del servidor: ")
        print (data['value'])
        
    else:
        print ("error al realizar la solicitud")
    


def chistesChuckNorrisList ():
    urlGet = "https://api.chucknorris.io/jokes/categories"
    getResponse = req.get (urlGet)
    
    if getResponse.status_code == 200:
        data = getResponse.json()
        
        print ("respuesta del servidor: ")
        print (data)
        
    else:
        print ("error al realizar la solicitud")



def chistesChuckNorrisCategorias (category):
    urlGet = f"https://api.chucknorris.io/jokes/random?category={category}"
    getResponse = req.get (urlGet)
    
    if getResponse.status_code == 200:
        data = getResponse.json()
        
        print ("respuesta del servidor: ")
        print (data['value'])
        
    else:
        print ("error al realizar la solicitud")

def menuPrograma():
    print ("menu de categorias")
    print ("presiona 1 para ver un chiste aleatorio de Chuck Norris")
    print ("presiona 2 para ver la lista de categorias de chistes de Chuck Norris")
    print ("presiona 3 para escoger un chiste con tu categoria preferida")
    print ("presiona 4 para termimar el programa")


while True:
    menuPrograma()
    
    menuCategoria = input("escribe tu opcion: \n")
    
    try:
        menuCategoria = int(menuCategoria)
    except ValueError:
        print("Opción inválida. Debes ingresar un número entero.")
        continue
    
    if menuCategoria == 1:
        chistesChuckNorris()
        
    elif menuCategoria == 2:
        chistesChuckNorrisList()
    
    elif menuCategoria == 3:
        categorias = input ("escribe el nombre de la categoria: \n")
        chistesChuckNorrisCategorias (categorias)
    
    elif menuCategoria == 4:
        print ("chaoooo!!!")
        break
    else:
        print ("no reconozco esa opcion, intenta de nuevo")
        
