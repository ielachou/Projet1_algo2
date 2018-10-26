import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#zizi de aris
class Tree():
    def __init__(self, root, val, children=[]):
        self.root = root
        self.val = val
        # each child is in the list
        self.children = children
        # Sum of all of nodes's values
        self.sum = 0
        self.graph = None

    def getVal(self):
        return self.val

    def getSum(self):
        return self.sum

    def get_subSum(self, res = 0):
        if self.getChildren() == []:
            res += self.getVal()
        else:
            rest = 0
            for c in self.getChildren():
                rest += c.get_subSum(res)
            res+= self.getVal()+rest
        return res

    def addChild(self, child):
        self.getChildren().append(child)

    def getChildren(self):
        return self.children

    def getRoot(self):
        return self.root

    def deepSearch(self):
        pass

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

    def printGraph(self):
        G = self.MakeGraph()
        # Je sais absolument pas ce que c'est mdr (j'pense ça dessine juste les sommets)
        plt.figure()
        pos_nodes = nx.spring_layout(G)
        pos_nodes = self.setCoord(pos_nodes)
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
        G.remove_nodes_from(nx.isolates(G))
        nx.draw_networkx_labels(G, pos_attrs, labels=custom_node_attrs)
        self.graph = G
        plt.show()

    def setCoord(self, coord, width=1., dy=0.2, x=0.5, y=0):
        coord[self.root] = np.array([x, y])
        if len(self.children) != 0:
            dx = width / len(self.children)
            newx = x - width / 2 - dx / 2
        for i in range(len(self.children)):
            newx += dx
            self.children[i].setCoord(coord, width=dx, dy=dy, x=newx, y=y - dy)
        return coord

    def max_subtree2(self, G, somme=0):
        a = False
        somme += self.val
        i = 0
        while i < len(self.children):
            if len(self.children[i].children) == 0:
                if self.children[i].getVal() < 0 or somme + self.children[i].getVal() <= 0:
                    G.remove_node(self.children[i].getRoot())
                    del self.children[i]
                    i -= 1
                    a = True
            else:
                self.children[i].max_subtree(G, somme)
            if a:
                self.max_subtree(G, somme)
            i += 1

    def deep_suppr(self):
        pass

    def max_subtree(self, G):
        i = 0
        while i < len(self.getChildren()):
            self.getChildren()[i].max_subtree(G)
            if self.getChildren()[i].get_subSum() <= 0:
                G.remove_node(self.getChildren()[i].getRoot())
                del self.getChildren()[i]
                print(self.getChildren())
                i-=1
            i+=1


a = Tree("r", 2, [Tree("a", -5, [Tree("c", 4), Tree("d", -1, [Tree("i", 4), Tree("j", -5, [Tree("l", -1), Tree("m", 3, [
    Tree("n", -1)])])]), Tree("e", -1)]), Tree("b", -1, [Tree("f", -1), Tree("g", -2, [Tree("k", 1)]), Tree("h", 2)])])


print(a.get_subSum())
a.printGraph()
#a.max_subtree2(a.graph)
a.max_subtree(a.graph)
a.printGraph()
