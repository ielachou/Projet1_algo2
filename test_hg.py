import hypergraph as hg

def test(n):
    ex = [[1,0,0,0],
          [1,1,0,0],
          [1,1,1,0],
          [0,0,0,1],
          [0,0,1,0],
          [0,0,1,0],
          [0,0,0,0]]

    if n == 1 : #affcihage normal
        test = hg.Hypergraph(ex)
        print(test.test_hypertree())


    elif n == 2: #affichage avec matrice aléatoire
        ex = hg.randomHypergraph()
        print("Matrice d'incidence: \n",ex,"\n")
        test = hg.Hypergraph(ex)
        print(test.test_hypertree())

if __name__ == '__main__':
    test(1)
