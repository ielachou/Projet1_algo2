import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import randint


class Tree():
    def __init__(self, root, val, children=[]):
        self.root = root
        self.val = val
        # each child is in the list
        if children == []:
            self.children = []
        else:
            self.children = children
        # Sum of all of nodes's values
        self.sum = 0
        self.graph = None

    def add_child(self, tree):
        self.children.append(tree)

    def getVal(self):
        return self.val

    def get_subSum(self, res = 0):
        if self.getChildren() == []:
            res += self.getVal()
        else:
            res_t = 0
            for c in self.getChildren():
                res_t += c.get_subSum(res)
            res+= self.getVal()+res_t
        return res

    def getChildren(self):
        return self.children

    def getRoot(self):
        return self.root

    def MakeGraph(self, G=nx.Graph()):  # Anciennement PrintTree
        # print(s)elf.root)
        # On ajoute un tuple dans la liste (noeud, valeur)
        G.add_node(self.root, val=self.val)
        for c in self.children:
            G.add_edge(c.root, self.root)
            c.MakeGraph(G)
        return G

    def __repr__(self):
        return "Tree de père " + str(self.getRoot())+ " "

    def printGraph(self, subbed = False):
        G = self.MakeGraph()
        #Create a matplot figure window
        plt.figure(1)
        pos_nodes = nx.spring_layout(G)
        posy = -1 if subbed else 0
        pos_nodes = self.setCoord(pos_nodes, y = posy)
        dico_isolated = nx.floyd_warshall(G)['r']
        for val in dico_isolated:
            if dico_isolated[val] == float('inf'):
                G.remove_node(val)
        nx.draw(G, pos_nodes, with_labels=True)
        # On va juste prendre les cordonnées pour pouvoir placer le label
        pos_attrs = {}
        for node, coords in pos_nodes.items():
            pos_attrs[node] = (
                coords[0] + 0.02, coords[1] + 0.04)  # Change le 0.05 ou même rajoute une valeur pour l'cordonnées
            # pour changer la position du label
        # C'est ici qu'on va associé chaques label à chaques noeud
        node_attrs = nx.get_node_attributes(G, 'val')
        custom_node_attrs = {}
        for node, attr in node_attrs.items():
            custom_node_attrs[node] = attr
        # Draw special pour afficher la valeur avec la possition par rapport au noeud
        nx.draw_networkx_labels(G, pos_attrs, labels=custom_node_attrs)
        self.graph = G

    def setCoord(self, coord, width=1., dy=0.2, x=0.5, y=0):
        coord[self.root] = np.array([x, y])
        if len(self.children) != 0:
            dx = width / len(self.children)
            newx = x - width / 2 - dx / 2
        for i in range(len(self.children)):
            newx += dx
            self.children[i].setCoord(coord, width=dx, dy=dy, x=newx, y=y - dy)
        return coord


    def max_subtree(self, G):
        i = 0
        while i < len(self.getChildren()):
            self.getChildren()[i].max_subtree(G)
            if self.getChildren()[i].get_subSum() <= 0:
                G.remove_node(self.getChildren()[i].getRoot())
                del self.getChildren()[i]

                i-=1
            i+=1


def random_tree(tree, n, noms=['r'], c = 97):
    if n >0:
        nbChilds = randint(0,3)
        if nbChilds == 0 and tree.getRoot() == 'r':
            nbChilds = randint(1,3)
        n-=nbChilds
        for i in range(nbChilds):
            char = chr(c+i)
            j = 1
            while char in noms:
                char = chr(c+j+i)
                j+=1
            noms.append(char)
            tree.add_child(random_tree(Tree(char,randint(-5,5)), n-i-1, noms, c+i+j))

    return tree








if __name__ == 'main':
    a = Tree("r", 2,
             [Tree("a", -5, [Tree("c", 4), Tree("d", -1, [Tree("i", 4), Tree("j", -5, [Tree("l", -1), Tree("m", 3, [
                 Tree("n", -1)])])]), Tree("e", -1)]),
              Tree("b", -1, [Tree("f", -1), Tree("g", -2, [Tree("k", 1, [Tree("z", 1)])]), Tree("h", 2)])])
    a.printGraph()
    a.max_subtree(a.graph)
    a.printGraph(subbed=True)
    plt.show()
    a.graph.clear()

    a = random_tree(Tree('r',randint(-5,5)),10)
    a.printGraph()
    a.max_subtree(a.graph)
    a.printGraph(subbed = True)
    plt.show()
