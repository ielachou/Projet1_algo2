import hypergraph as hg

def test(n):
    """
    [[0 1 0 0]]
Cliques :  [['v1']]
Chordal ? :  True
{}
ok


[[0]
 [0]
 [1]
 [1]
 [0]]
Cliques :  [['Ev1']]
Chordal ? :  True
{'E1': ['Ev4', 'Ev3']}
L'hypergraphe est un hypertree


    """
    ex = [[1,0,0,0],
          [1,1,0,0],
          [1,1,1,0],
          [0,0,0,1],
          [0,0,1,0],
          [0,0,1,0],
          [0,0,0,0]]
    ex2 =[[1, 1, 1, 0, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 0, 1, 0, 0, 0]]
    if n == 1 : #affcihage normal
        test = hg.Hypergraph(ex)
        isHT = test.test_hypertree()


    elif n == 2: #affichage avec matrice aléatoire
        ex = hg.randomHypergraph()
        print(ex)
        test = hg.Hypergraph(ex)
        isHT = test.test_hypertree()

if __name__ == '__main__':
    test(1)
