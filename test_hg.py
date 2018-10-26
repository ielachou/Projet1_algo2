import hypergraph as hg

ex = [[1,0,0,0],
      [1,1,0,0],
      [1,1,1,0],
      [0,0,0,1],
      [0,0,1,0],
      [0,0,1,0],
      [0,0,0,0]]
#test = hg.Hypergraph(ex)

ex2 = hg.randomHypergraph(7,5)
hg.Hypergraph(ex2)
