#!/usr/local/bin/python3.6
#  versión en python 3.6
#  proposito: genera un archivo de llamadas de IVR
#
import sys
from random import randint
from datetime import datetime


def main():

    qllamadas = 1000
    qcuid = 20

    arbol = { 1:[2,2,2,3,4,5]
            , 2:[5,6,7,1], 3:[8,8,9,9,10,1], 4:[11,12,13,13,1]
            , 5:[14,15,15,15,16,1]
            }

    for caid in range(1, qllamadas +1):
        cuid = randint(1, qcuid)
        node = 1
        while node > 0:
            print( caid, cuid, node)
            try:
                lista = arbol[ node]
                largo = len( lista)
                elegido = randint(0, largo)
                if elegido != largo:
                    node = lista[ randint(0, largo - 1) ]
                else:
                    print( caid, cuid, "a")
                    break
            except:
                node = -1
                print( caid, cuid, "z")

    return


if __name__ == "__main__":
    main()
