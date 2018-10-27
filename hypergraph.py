import networkx as nx
import matplotlib.pyplot as plt
from random import randint
import numpy as np

"""
Matrice d'incidence pour afficher l'hypergraphe
"""
class Hypergraph():
    def __init__(self, M = [[]], type = "I"):
        self.mat = M

        self.nodes = len(M)
        self.edges = len(M[0])
        if type == "I":
            self.incidence = self.incidenceHG()
        elif type == "P":
            self.primal = self.primalHG()

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

        nx.draw(HG, pos_nodes, with_labels = True, node_color = "#61FDD9", node_size = 600)
        plt.show()

        return HG

    def primalHG(self):
        HG = nx.Graph()
        M = self.getMat()

        for i in range(len(M[0])):
            same_edge = []
            for j in range(len(M)):
                #####OPTIMISER
                if not 1 in M[j]:
                    HG.add_node("v" + str(j+1))
                if M[j][i] == 1:
                    same_edge.append("v" + str(j+1))

            if len(same_edge) > 1:
                same_edge.append(same_edge[0])
                HG.add_path(same_edge)
            elif len(same_edge) == 1:
                HG.add_node(same_edge[0])

        nx.draw(HG, with_labels = True, node_color = "#6160D9", node_size = 600)
        plt.show()
        return HG







def randomHypergraph(v = 0, E = 0):
    if v == 0 and E == 0:
        return np.random.randint(2, size=(randint(1,7),(randint(1,7))))
    else:
        return np.random.randint(2, size=(v,E))
