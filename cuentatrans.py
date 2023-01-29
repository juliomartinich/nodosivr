#!/usr/local/bin/python3.6
#  versión en python 3.6
#  proposito: lee un archivo de transciones y genera conteo
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
    transiciones = {}
    with open(nom_in, mode="r") as archin:
        for line in archin:
            token = line.split()
            trans = token[2]
            if trans in transiciones:
                transiciones[trans] += 1
            else:
                transiciones[trans] = 1


    for trans in transiciones:
        print(trans, transiciones[trans])

    return


if __name__ == "__main__":
    main()
