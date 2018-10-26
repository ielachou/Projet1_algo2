import networkx as nx
import matplotlib.pyplot as plt

a = nx.Graph()
a.add_edges_from([(1,2),(2,3), (2,4)])

b = nx.Graph()
b.add_edges_from([('r','e'),('e','t'),('e','g')])

plt.figure("Initial")
nx.draw(a)
nx.draw(b)
plt.show()