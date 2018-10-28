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
        test.test_hypertree()
        #test.drawHG()
    elif n == 2: #affichage avec matrice aléatoire
        ex = hg.randomHypergraph()
        print(ex)
        hg.Hypergraph(ex,type)
if __name__ == '__main__':
    test(1)
