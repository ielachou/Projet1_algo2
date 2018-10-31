import hypergraph as hg

def test(n,type = "I"):
    ex = [[1,0,0,0],
          [1,1,0,0],
          [1,1,1,0],
          [0,0,0,1],
          [0,0,1,0],
          [0,0,1,0],
          [0,0,0,0]]
    ex2 =[[1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0]]
    if n == 1 : #affcihage normal
        test = hg.Hypergraph(ex2,type)
        test.test_hypertree()
        test.drawHG()
    elif n == 2: #affichage avec matrice aléatoire
        ex = hg.randomHypergraph()
        print(ex)
        test = hg.Hypergraph(ex,type)
        test.test_hypertree()
if __name__ == '__main__':
    test(1)
