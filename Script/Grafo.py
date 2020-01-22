from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
from numpy import *

#-----------------------------------
# Nombres: Juan Pablo Quezada
#          Alfonso Duarte
# Curso: Teoria de Grafos
# Profesor: Gabriel Venegas
#-----------------------------------

class Arbol:
    #---------------------------------------------------------------
    #  Inicializacion de Variables
    #---------------------------------------------------------------
    def __init__(self):
        self.nVertices = "" #variable que almacenara la cantidad de vertices del arbol.
        self.aMA = [] # arreglo que almacenara la matriz de adyacencia.
        self.aVertice = [] #array que contendra los vertices representados con letras(ASCII).
        self.G = nx.Graph() # Inicializamos un grafo vacio.
        self.cNodo = {} # varible que almacenara el color del nodo.
    #----------------------------------------------------------
    # Metodo encargado de Pedir Datos de Matriz de adyacencia
    #----------------------------------------------------------
    def Input_MA(self): 
        for i in range(int(self.nVertices)): #recorre filas en el largo de los vertices.
            a = [] # inicializamos un array que contendra las filas de la matriz.
            for j in range(int(self.nVertices)): # recorremos la columnas de las filas.
                while True: # iniciamos un bucle infino hasta que ingrese datos correctamente.
                    dat = raw_input("Ingrese datos de la fila "+str(i+1)+":") #pedidos datos de la fila
                    if dat.isdigit(): #si el dato es digito...
                        a.append(int(dat)) #lo ingresamos al array
                        break #rompemos el while
                    print "dato mal ingresado, intentelo nuevamente.."
            self.aMA.append(a) # ingresamos la fila a la matriz
        return self.aMA #retornamos la matriz
    #----------------------------------------------------------------
    # Metodo encargado de Pedir el numero de Vertices, que tendra
    # que tendra el Arbol, para luego determinar como sera la matriz
    #----------------------------------------------------------------
    def Input_nVertice(self):
        while True: # iniciamos un bucle infino hasta que ingrese datos correctamente.
            self.nVertices = raw_input("Ingrese numero de Vertices: ") # pedimos el numero de vertices.
            if self.nVertices.isdigit(): # si el dato es un numero...
                for i in range(int(self.nVertices)): #recorremos en el rango de los vertices
                    self.aVertice.append(chr(65+i)) #Generamos letras en un formato ascii
                break # rompemos el ciclo.
        return self.aVertice # retornamos un array con los vertices generados en letras.
    #---------------------------------------------------------------
    #  Metodo que pide cual sera el Vertice raiz
    #---------------------------------------------------------------
    def Input_Vertice_Raiz(self):
        ok = True  # bandera para salir del ciclo
        while ok: # iniciamos un bucle hasta que ingrese datos correctos
            raiz = raw_input("Ingrese un Nodo Raiz: ").upper() # pedimos el nodo raiz
            for i in range(len(self.aVertice)): # recorremos en el rango del array de vertices
                if self.aVertice[i] == raiz:# si nodo raiz es igual a alguno de los vertices designados..
                    print "Su nodo raiz sera: ",raiz,"\n" # imprimimos su nodo raiz
                    self.cNodo = {self.aVertice[i]: 1.0} # designados el nodo raiz con un contraste  distinto.
                    ok = False #  paramos el ciclo.
        return self.cNodo # retornamos el color del nodo.
    #---------------------------------------------------------------
    #  Metodo que genera el arbol
    #---------------------------------------------------------------
    def Generate_Arbol(self):
        for row in range(int(self.nVertices)): # recorremos las filas en el rango de los vertices
            for column in range(int(self.nVertices)): # recorremos la columnas en el rango de los vertices
                if self.aMA[row][column]==1: # si en la fila o columna correspondiente encuantra un 1...
                    # se crea la arista desde un vertice a otro ej: de A a B, y luego de B a A
                    # y solo asi se mostrata la arista entre los vertices en el arbol. 
                    self.G.add_edge(self.aVertice[row],self.aVertice[column]) 
                    self.G.add_edge(self.aVertice[column],self.aVertice[row])
        self.Valida_Arbol() # Llama a la funcion que validara si es un arbol
    #---------------------------------------------------------------
    #  Metodo que valdia si el grafo que se genero es un arbol
    #---------------------------------------------------------------
    def Valida_Arbol(self):
        if nx.is_tree(self.G): #  verifica si el grafo generado es un arbol o no.
            values = [self.cNodo.get(node, 0.8) for node in self.G.nodes()] # obtenemos los nodos
            pos = nx.spring_layout(self.G) # su posicion
            nx.draw(self.G, pos,cmap=plt.get_cmap('jet') ,node_color=values) # y los dibujamos vertices
            nx.draw_networkx_labels(self.G, pos) # dibujamos las letras
            print "La matriz de adyacencia ingresada  SI Corresponde a un Arbol (:"
            plt.savefig('this.png') #guardamos la imagen
            plt.show() # y la mostramos
        else:
            print "La matriz de adyacencia ingresada NO corresponde a un Arbol!"
