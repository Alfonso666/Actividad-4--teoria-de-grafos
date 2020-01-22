from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
from numpy import *
from Script import Grafo as gf

vertices = []
def main():
    arbol = gf.Arbol()
    #------------------------------------------
    #       Mostrar vertices del Arbol
    #------------------------------------------
    vertices = arbol.Input_nVertice()
    print"+--------------------------------------+"
    print " Los vertices seran los siguientes: \n "
    print"+--------------------------------------+"
    print " "*8,vertices,"\n"
    print"+--------------------------------------+"
    print "Su Matriz de adyacencia sera de: ", len(vertices),"x", len(vertices),"\n"

    print "Seleccione la Raiz del Arbol Ejemplo: A, B o C \n"
    arbol.Input_Vertice_Raiz()
    #------------------------------------------
    #       pedir datos Matriz Adyacencia
    #------------------------------------------
    print " Ingrese Matriz de Adyacencia: \n "
    print"+--------------------------------------+"
    arbol.Input_MA()
    #-----------------------------------------------
    #       Generacion del Arbol
    #-----------------------------------------------
    arbol.Generate_Arbol()



if __name__ == '__main__':
    main()
