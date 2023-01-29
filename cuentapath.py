#!/usr/local/bin/python3.6
#  versión en python 3.6
#  proposito: lee un archivo de path y genera conteo de path
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
    path = ""
    caminos = {}
    with open(nom_in, mode="r") as archin:
        for line in archin:
            token = line.split()
            path = token[2]
            if path in caminos:
                caminos[path] += 1
            else:
                caminos[path] = 1


    for path in caminos:
        print( caminos[path], path)

    return


if __name__ == "__main__":
    main()
