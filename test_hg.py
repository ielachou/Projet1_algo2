import hypergraph as hg

def test(n,type = "I"):
    ex = [[1,0,0,0],
          [1,1,0,0],
          [1,1,1,0],
          [0,0,0,1],
          [0,0,1,0],
          [0,0,1,0],
          [0,0,0,0]]

    if n == 1 : #affcihage normal
        test = hg.Hypergraph(ex,type)

    elif n == 2: #affichage avec matrice aléatoire
        ex = hg.randomHypergraph()
        hg.Hypergraph(ex,type)

    elif n == 3: #affichage graphe primal
        test = hg.Hypergraph(ex,type)



test(1,"P")
