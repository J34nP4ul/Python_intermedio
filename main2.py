import api
import requests
import ids
import time


from api import getOneUser
from ids import ids as lista

def progLineal():
    tiempoInicial = time.time()
    for ids in lista:
        nuevaLista = getOneUser(ids)
        print(f"Nombre del usuario con ID {ids}: {nuevaLista}")

    tiempoFinal = time.time()
    tiempoTotal = tiempoFinal - tiempoInicial

    print(f"Tiempo de duración: {tiempoTotal} segundos")
    
progLineal()

# import api
# import requests
# import ids
# import time
# import concurrent.futures

# from api import getOneUser
# from ids import ids as ids_list

# def progCurrent(id):
#     nuevaLista = getOneUser(id)
#     print(f"Nombre del usuario con ID {id}: {nuevaLista}")

# tiempoInicial = time.time()

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(progCurrent, ids_list)

# tiempoFinal = time.time()
# tiempoTotal = tiempoFinal - tiempoInicial

# print(f"Tiempo de duración: {tiempoTotal} segundos")

# import api
# import requests
# import ids
# import time
# import multiprocessing

# from api import getOneUser
# from ids import ids as ids_list

# def consultar_usuario(id):
#     nuevaLista = getOneUser(id)
#     print(f"Nombre del usuario con ID {id}: {nuevaLista}")

# if __name__ == '__main__':
#     tiempoInicial = time.time()

#     with multiprocessing.Pool() as pool:
#         pool.map(consultar_usuario, ids_list)

#     tiempoFinal = time.time()
#     tiempoTotal = tiempoFinal - tiempoInicial

#     print(f"Tiempo de duración: {tiempoTotal} segundos")
