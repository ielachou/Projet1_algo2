import networkx as nx
import matplotlib.pyplot as plt

class Tree():
    def __init__(self, root,val, children = []):
        self.root = root
        self.val = val
        #each child is in the list
        self.children = children
        #Sum of all of nodes's values
        self.sum = 0
        self.graph = nx.Graph()

    def getVal(self):
        return self.val

    def getSum(self):
        return self.sum

    def getChildren(self):
        return self.children

    def deepSearch(self):
        pass


    def printTree(self,G, a =[]):
        print(self.root)
        a.append(self.root)
        for c in self.children:
            G.add_edge(c.root,self.root)
            c.printTree(G, a)
        return a

    def printGraph(self):
        G = nx.Graph()
        NodeList = self.printTree(G)
        print(NodeList)
        G.add_nodes_from(NodeList)
        nx.draw(G, with_labels = True)
        plt.show()


a = Tree("r", 2, [Tree("a", -5,[Tree("c", 4),Tree("d",-1),Tree("e", -1)]),Tree("b",-1, [Tree("f", -1), Tree("g", -2), Tree("h",2)])])
a.printGraph()