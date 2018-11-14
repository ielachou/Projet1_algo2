from tree import *
from test_hg import *
import matplotlib.pyplot as plt


def main():
    rep = 0
    print("Bienvenue sur le projet d'algo d'Achraf et Iliass !\n")
    while rep != "3":
        print("Sélectionnez la section du projet que vous voulez utiliser : \n"
              "1 : Sous-arbre de poids maximum\n"
              "2 : Les hypergraphes et hypertrees\n"
              "3 : Quitter\n")
        rep = ""
        while rep not in ["1", "2", "3"]:
            rep = input()
            if rep not in ["1", "2", "3"]:
                print("Entrez 1, 2 ou 3 !")
        if rep == "1":
            print("1) ")
            a = Tree("r", 2,
                     [Tree("a", -5,
                           [Tree("c", 4), Tree("d", -1, [Tree("i", 4), Tree("j", -5, [Tree("l", -1), Tree("m", 3, [
                               Tree("n", -1)])])]), Tree("e", -1)]),
                      Tree("b", -1, [Tree("f", -1), Tree("g", -2, [Tree("k", 1, [Tree("z", 1)])]), Tree("h", 2)])])
            print("Exemple de l'énoncé, fermez la fenêtre pour accéder à la suite.")
            execute(a)
            a = random_tree(Tree('r', randint(-5, 5)), 10)
            print("Exemple aléatoire, fermez la fenêtre pour accéder à la suite.")
            execute(a)
        elif rep == "2":
            print("Exemple de l'énoncé, fermez les fenêtres pour accéder à la suite.")
            test(1)
            print("Exemple aléatoire, fermez les fenêtres pour accéder à la suite.")
            test(2)


if __name__ == '__main__':
    main()
