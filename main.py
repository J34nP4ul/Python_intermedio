import api
import requests
import ids
import time
import cProfile
import pstats

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
    
def progConcurrencia():
    tiempoInicial = time.time()
    for ids in lista:
        nuevaLista = getOneUser(ids)
        print(f"Nombre del usuario con ID {ids}: {nuevaLista}")

    tiempoFinal = time.time()
    tiempoTotal = tiempoFinal - tiempoInicial

    print(f"Tiempo de duración: {tiempoTotal} segundos")
#   
def main ():
    #progLineal()
    progConcurrencia()

if __name__ == '__main__':
    cProfile.run('main()', filename='profiling_results')

stats = pstats.Stats('profiling_results')
stats.sort_stats('cumulative')
stats.print_stats()
