import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np

"""
Matrice d'incidence pour afficher l'hypergraphe
"""
class Hypergraph():
    def __init__(self, M = [[]], type = ""):

        self.mat = M
        self.trans = self.transpo()
        self.nodes = len(M)
        self.edges = len(M[0])

        self.incidence = self.incidenceHG()
        self.dual = self.dualHG()
        self.primal = self.primalHG()
        #self.test_hypertree()
        """
        if type == "I":
            self.drawHG(self.incidence[1])
        elif type == "P":
            self.drawHG(self.primal[1])
        else:
            self.drawHG()
        """

    def getNbrNodes(self):
        return self.nodes

    def getNbrEdges(self):
        return self.edges

    def getMat(self):
        return self.mat

    def incidenceHG(self):
        M = self.getMat()
        HG = nx.Graph()
        pos_nodes = {}

        j = 0
        for i in range(len(M)):
            HG.add_node("v" + str(i+1))
            pos_nodes["v" + str(i+1)] = np.array([0, 10 - i])

            for j in range(len(M[0])):
                if M[i][j]:
                    curr_edge = "E" + str(j+1)
                    if curr_edge not in HG.edges():
                        HG.add_node("E" + str(j+1))
                    pos_nodes["E" + str(j+1)] = np.array([5, 10 - j])
                    HG.add_edge("v" + str(i+1),"E" + str(j+1))
        fig = plt.figure("Graphe d'incidence")
        nx.draw(HG, pos_nodes, with_labels = True, node_color = "#e416ff", node_size = 600)
        return HG

    def dualHG(self):

        M = self.trans
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

        fig = plt.figure("Graphe dual")
        nx.draw(HG, pos_nodes, with_labels = True, node_color = "#fd16a4", node_size = 600)
        return HG


    def primalHG(self):
        HG = nx.Graph()
        M = self.trans

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

        fig = plt.figure("Graphe primal")
        nx.draw(HG, with_labels = True, node_color = "#6e16fd", node_size = 600)
        return HG

    def checkClique(self):
        primal = self.primal
        dual = self.dual
        dic_edge = {}
        for i in range(self.edges):
            E_i = "E" + str(i+1)
            curr_edges = dual.edges(E_i)
            if len(curr_edges) >= 2:
                for edge in curr_edges:
                    if E_i not in dic_edge:
                        dic_edge[E_i] = [edge[1]]
                    else:
                        dic_edge[E_i].append(edge[1])

        print(dic_edge)

        cliques = list(nx.find_cliques(primal))
        res = True
        while len(cliques) != 0:
            clique = cliques.pop()
            if len(clique) >= 2:
                clique.sort()
                #print("pop :", clique)

                finded = False

                for edge in dic_edge:
                    dic_edge[edge].sort()
                    if dic_edge[edge] == clique:
                        finded = True
                if finded == False:
                    return finded

        return True




    def test_hypertree(self):
        primal = self.primal

        print("Cliques : ", list(nx.find_cliques(primal)))
        print("Chordal ? : ", nx.is_chordal(primal))
        a  = self.checkClique()
        if nx.is_chordal(primal) and a:
            print("ok")


            plt.show()
        else:
            print("pas ok")
            plt.show()
            return False

    def transpo(self):
        M = self.getMat()
        liste = [[0 for j in range(len(M))] for i in range(len(M[0]))]
        for j in range(len(liste)):
            for i in range(len(liste[0])):
                liste[j][i] = M[i][j]
        return liste

    def drawHG(self):
        plt.show()




def randomHypergraph(v = 0, E = 0):
    if v == 0 and E == 0:
        return np.random.randint(2, size=(randint(1,7),(randint(1,7))))
    else:
        return np.random.randint(2, size=(v,E))
    plt.show()
