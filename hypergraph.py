import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np

"""
Matrice d'incidence pour afficher l'hypergraphe
"""
class Hypergraph():
    def __init__(self, M = [[]]):

        self.mat = M
        self.trans = self.transpo()

        self.nodes = len(M)
        self.edges = len(M[0])

        self.incidence = self.incidenceHG()
        self.dual = self.dualHG()
        self.primal = self.primalHG()

    #simple getter et setter
    def getNbrEdges(self):
        return self.edges

    def getMat(self):
        return self.mat

    def getTrans(self):
        return self.trans

    def getIncidence(self):
        return self.incidence

    def getDual(self):
        return self.dual

    def getPrimal(self):
        return self.primal

    def incidenceHG(self):
        """
        Méthode qui va initialiser et dessiner le graphe d'incidence
        via la matrice d'getIncidence
        """
        M = self.getMat()
        #initialisation du graphe
        HG = nx.Graph()
        #dictionnaire qui va contenir les positions des différents
        #noeuds pour les afficher comme dans l'énoncé
        pos_nodes = {}

        j = 0
        for i in range(len(M)):
            #ici on ajoute le sommet et on initialise sa position
            HG.add_node("v" + str(i+1))
            pos_nodes["v" + str(i+1)] = np.array([0, 10 - i])

            for j in range(len(M[0])):
                #même chose qu'en haut, on va créer l'hyperarrête si il y a au
                #moins un lien avec
                if M[i][j]:
                    curr_edge = "E" + str(j+1)
                    if curr_edge not in HG.edges():
                        HG.add_node("E" + str(j+1))
                    pos_nodes["E" + str(j+1)] = np.array([5, 10 - j])
                    HG.add_edge("v" + str(i+1),"E" + str(j+1))
        plt.figure("Graphe d'incidence")
        nx.draw(HG, pos_nodes, with_labels = True, node_color = "#e416ff", node_size = 600)
        return HG

    def dualHG(self):
        M = self.getTrans()
        HG = nx.Graph()

        pos_nodes = {}

        j = 0
        for i in range(len(M)):
            HG.add_node("E" + str(i+1))
            pos_nodes["E" + str(i+1)] = np.array([0, 10 - i])

            for j in range(len(M[0])):
                if M[i][j]:
                    curr_edge = "Ev" + str(j+1)
                    if curr_edge not in HG.edges():
                        HG.add_node("Ev" + str(j+1))#Ev
                    pos_nodes["Ev" + str(j+1)] = np.array([5, 10 - j])#Ev
                    HG.add_edge("E" + str(i+1),"Ev" + str(j+1))#Ev

        plt.figure("Graphe dual")
        nx.draw(HG, pos_nodes, with_labels = True, node_color = "#fd16a4", node_size = 600)
        return HG


    def primalHG(self):
        HG = nx.Graph()
        M = self.getTrans()

        for i in range(len(M[0])):
            same_edge = []
            for j in range(len(M)):
                #####OPTIMISER##################################
                if not 1 in M[j]:
                    HG.add_node("Ev" + str(j+1))
                if M[j][i] == 1:
                    same_edge.append("Ev" + str(j+1))
            #print(same_edge)
            if len(same_edge) > 1:
                same_edge.append(same_edge[0])
                HG.add_path(same_edge)
            elif len(same_edge) == 1:
                HG.add_node(same_edge[0])

        plt.figure("Graphe primal")
        nx.draw(HG, with_labels = True, node_color = "#6e16fd", node_size = 600)
        return HG

    def checkClique(self): #O(m²n²)
        primal = self.getPrimal() #O(1)
        dual = self.getDual() #O(1)
        dic_edge = {} #O(1)
        for i in range(self.getNbrEdges()): #O(m)
            E_i = "E" + str(i+1) #O(1)
            curr_edges = dual.edges(E_i) #O(1)
            if len(curr_edges) >= 2: #0(1)
                for edge in curr_edges: #O(m)
                    if E_i not in dic_edge: #O(n)
                        dic_edge[E_i] = [edge[1]] #O(1)
                    else:
                        dic_edge[E_i].append(edge[1]) #O(n)

        print(dic_edge)

        cliques = list(nx.find_cliques(primal)) #O(3^(n/3))
        finded = False #O(1)
        #O(l²m²log(m)log(l))
        while len(cliques) != 0: #O(l) l = nombre de cliques
            clique = cliques.pop() #O(1)
            if len(clique) >= 2: #O(1)
                clique.sort() #O(l log l)

                finded = False #O(1)

                #O(m²log(m))
                for edge in dic_edge: #O(m)
                    dic_edge[edge].sort() #O(m log m)
                    if dic_edge[edge] == clique: #O(1)
                        finded = True #O(1)
                if finded == False: #O(1)
                    return False #O(1)

        return finded



    #O(m²n²)
    def test_hypertree(self):
        primal = self.getPrimal()

        print("Cliques : ", list(nx.find_cliques(primal)))
        print("Chordal ? : ", nx.is_chordal(primal))
        isClique  = self.checkClique() #O(m²n²)
        isChodal = nx.is_chordal(primal) #O(m*n)
        if isChodal and isClique:
            plt.show()
            return True
        else:
            plt.show()
            return False

    #O(m*n)
    def transpo(self):
        M = self.getMat()
        liste = [[0 for j in range(len(M))] for i in range(len(M[0]))]
        for j in range(len(liste)):
            for i in range(len(liste[0])):
                liste[j][i] = M[i][j]
        return liste





def randomHypergraph(v = 0, E = 0):
    if v == 0 and E == 0:
        return np.random.randint(2, size=(randint(1,7),(randint(1,7))))
    else:
        return np.random.randint(2, size=(v,E))
    plt.show()
