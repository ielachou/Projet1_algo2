import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np
from random import randint

class randomNode(object):
    ind = 0
    def __init__(self, n = 0):
        self.nodes = n
        self.g = self.creat()

    def creat(self):
        G = nx.Graph()
        for i in range(self.nodes):
            G.add_node(str(i))
        return G

    def draw(self):
        nx.draw(self.g)


class Index(object):
    ind = 0
    def __init__(self,listFig):
        self.fig = listFig

    def next(self, event):
        self.ind += 1
        i = self.ind %(len(self.fig))
        self.fig[i].draw()

    def prev(self, event):
        self.ind -= 1
        i  = self.ind %(len(self.fig))
        self.fig[i].draw()

node1 = randomNode(10)
node2 = randomNode(5)
NS = [node1, node2]

callback = Index(NS)
axprev = plt.axes([0.7, 0.05, 0.1, 0.075])
axnext = plt.axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)

plt.show()
