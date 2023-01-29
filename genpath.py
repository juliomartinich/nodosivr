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
            caid_old = caid
            cuid_old = cuid
            caid = lista[0]
            cuid = lista[1]
            if caid == caid_old:
                nodo = nodo + "-" + lista[2]
            else:
                if caid_old != "":
                    print(caid_old, cuid_old, nodo)
                nodo = lista[2]

    print(caid_old, cuid_old, nodo)


    return


if __name__ == "__main__":
    main()
