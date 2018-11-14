import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import time


class Tree():
    """
    Classe Tree qui instancie un arbre récursif, ou chaque noeud est lui même un Tree
    """

    def __init__(self, root, val, children=[]):
        """
        Constructeur de tree
        :param root: nom du Tree
        :param val: valeur du Tree
        :param children: Liste des enfants du Tree
        """
        self.root = root
        self.val = val
        # each child is in the list
        if children == []:
            self.children = []
        else:
            self.children = children
        self.graph = None

    def setVal(self, val):
        self.val = val

    def getVal(self):
        """
        Accesseur de la valeur du noeud
        :return: val
        """
        return self.val

    def getChildren(self):
        """
        Accesseur de la liste des enfants d'un Tree
        :return: children
        """
        return self.children

    def getRoot(self):
        """
        Accesseur du nom du noeud correspondant au Tree
        :return: root
        """
        return self.root

    def add_child(self, tree):
        """
        Ajoute un enfant à la liste des enfants du Tree
        :param tree: enfant à rajouter à l'objet Tree
        :return: Rien
        """
        self.children.append(tree)

    def MakeGraph(self, G=nx.Graph()):
        """
        Methode récursive qui crée le graphe networkx correspondant à un Tree
        :param G: Graphe networkx
        :return: Graphe du Tree
        """
        # On ajoute un tuple dans la liste (noeud, valeur), va permettre à l'affichage
        G.add_node(self.root, val=self.val)
        for c in self.children:
            G.add_edge(c.root, self.root)
            c.MakeGraph(G)
        return G

    def printGraph(self, subbed=False):
        """
        Méthode dessinant le graphe un Tree correctement, la valeur de ses noeuds, le nom des noeuds, ...
        :param subbed: True si on veut afficher l'arbre réduit, va décaler les coordonnées.
        :return: Rien
        """
        G = self.MakeGraph()
        # Crée une figure (fenêtre) matplot où sera affiché le graphe
        plt.figure("Sous arbre de poids maximum")
        pos_nodes = nx.spring_layout(G)
        posy = -1 if subbed else 0 #modifie la position en fonction de si on veut afficher l'arbre réduit ou l'initial
        pos_nodes = self.setCoord(pos_nodes, y=posy)
        dico_isolated = nx.floyd_warshall(G)['r']
        for val in dico_isolated:
            if dico_isolated[val] == float('inf'):
                G.remove_node(val)
        if self.getChildren() == [] and self.getVal() <= 0:
            G.remove_node("r")
            self.setVal(0)
        nx.draw(G, pos_nodes, with_labels=True)
        # On va juste prendre les cordonnées pour pouvoir placer le label
        pos_attrs = {}
        for node, coords in pos_nodes.items():
            pos_attrs[node] = (coords[0] + 0.02, coords[1] + 0.04)
            # pour changer la position du label
        # C'est ici qu'on va associé chaques label à chaques noeud
        node_attrs = nx.get_node_attributes(G, 'val')
        custom_node_attrs = {}
        for node, attr in node_attrs.items():
            custom_node_attrs[node] = attr
        # Draw special pour afficher la valeur avec la position par rapport au noeud
        nx.draw_networkx_labels(G, pos_attrs, labels=custom_node_attrs)
        self.graph = G


    def setCoord(self, coord, width=1., dy=0.2, x=0.5, y=0):
        """
        Méthode qui va permettre un affichage "clean" de l'arbre sous forme d'arbre balancé et égalisé.
        Inspiré de
        https://stackoverflow.com/questions/29586520/can-one-get-hierarchical-graphs-from-networkx-with-python-3
        :param coord: dictionnaire des positions en fonction du noeud
        :param width: écart horizontal entre deux noeuds de même degré
        :param dy: écart vertical entre un père et son fils
        :param x: abscisse initiale d'un Tree "père"
        :param y: ordonnée initiale d'un Tree "père"
        :return: coord, dictionnaire des positions modifiées
        """
        coord[self.root] = np.array([x, y])
        if len(self.children) != 0:
            dx = width / len(self.children)
            newx = x - width / 2 - dx / 2
        for i in range(len(self.children)):
            newx += dx
            self.children[i].setCoord(coord, width=dx, dy=dy, x=newx, y=y - dy)
        return coord

    def get_subSum(self, res=0):
        """
        Algorithme calculant la somme des poids totaux d'un Tree, en effectuant un parcours en profondeur
        Complexité : O(m)
        :param res: somme
        :return: somme des poids totaux d'un Tree
        """
        if self.getChildren() == []: #O(1)
            res += self.getVal() #0(1)
        else:
            res_t = 0  # Somme temporaire afin de l'ajouter totalement à res plus tard #O(1)
            for c in self.getChildren(): #O(m)
                res_t += c.get_subSum(res) #O(m = nombre de noeuds de l'arbre)
            res += self.getVal() + res_t #O(1)
        return res #0(1)

    def max_subtree(self, G):
        """
        Algorithme principal demandé. Supprime des noeuds s'il considère qu'ils ne contribuent au score max du Tree
        Complexité O(n*m)
        :param G: graphe networkx utilisé pour l'affichage
        :return: Rien
        """
        i = 0 #O(1)
        while i < len(self.getChildren()): #O(n*m)
            self.getChildren()[i].max_subtree(G) #O(n*m)
            if self.getChildren()[i].get_subSum() <= 0:#O(m)
                G.remove_node(self.getChildren()[i].getRoot())
                del self.getChildren()[i] #O(n)

                i -= 1 #O(1)
            i += 1 #O(1)

def random_tree(tree, n, noms, c=97):
    """
    Algorithme générateur d'arbre aléatoires avec chaque Tree qui a max 3 fils
    :param tree: Tree parent, va être initialisé avec tree = Tree("r", randint(-5,5))
    :param n: variable qui va permettre de limiter le nombre de noeuds à l'arbre
    :param noms: liste contenant les caractères déjà utilisés pour nommer un noeud, pour éviter les doublons
    :param c: caractère actuel pour nommer un noeud
    :return: Tree random avec des valeurs entre -5 et 5
    """
    if n > 0:
        nbChilds = randint(0, 3)
        if nbChilds == 0 and tree.getRoot() == 'r': #Fais en sorte d'avoir au moins un fils au noeud r
            nbChilds = randint(1, 3)
        n -= nbChilds
        for i in range(nbChilds):
            char = chr(c + i)
            j = 1
            while char in noms:
                char = chr(c + j + i)
                j += 1
            noms.append(char)
            tree.add_child(random_tree(Tree(char, randint(-5, 5)), n - i - 1, noms, c + i + j))

    return tree


def execute(tree):
    """
    affiche un Tree, son arbre réduit, et leurs poids respectifs
    :param tree: tree a réduire
    :return: Rien
    """
    tree.printGraph()
    print("Somme de l'arbre initial : " + str(tree.get_subSum()))
    tree.max_subtree(tree.graph)
    tree.printGraph(subbed=True)
    sum = tree.get_subSum()
    if sum <= 0:
        sum = "L'arbre enraciné en r n'a pas de sous arbre positif"
    print("Somme de l'arbre réduit : " + str(sum))

    plt.show()
    tree.graph.clear() #Efface le graphe networkx pour éviter les incohérences entre deux Tree
