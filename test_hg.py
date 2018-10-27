import hypergraph as hg

ex = [[1,0,0,0],
      [1,1,0,0],
      [1,1,1,0],
      [0,0,0,1],
      [0,0,1,0],
      [0,0,1,0],
      [0,0,0,0]]
#test = hg.Hypergraph(ex)

ex2 = hg.randomHypergraph()
hg.Hypergraph(ex2)
