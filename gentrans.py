#!/usr/local/bin/python3.6
#  versión en python 3.6
#  proposito: procesa un archivo de nodos de llamadas de IVR
#             y genera los path
#
import sys
from random import randint
from datetime import datetime

def main():

    try:
        nom_in = sys.argv[1] + ".txt"
    except IndexError:
        sys.exit("Eror: debe ingresar un nombre de archivo txt")    

    caid = ""
    cuid = ""
    nodo = ""
    with open(nom_in, mode="r") as archin:
        for line in archin:
            lista = line.split()
            caidold = caid
            cuidold = cuid
            caid = lista[0]
            cuid = lista[1]
            if caid == caidold and cuid == cuidold:
                nodo = nodo + "_" + lista[2]
                print( caid, cuid, nodo)
                nodo = lista[2]
            else:
                if caidold != "":
                    nodo = nodo + "_Z"
                    print(caidold, cuidold, nodo)
                nodo = lista[2]

    nodo = nodo + "_Z"
    print(caidold, cuidold, nodo)


    return


if __name__ == "__main__":
    main()
