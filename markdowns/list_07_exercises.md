# Exercice 1

Complétez la fonction `moyenne` prenant en entrée une liste de valeurs numériques et renvoyant la moyenne de ces valeurs.

@[Moyenne]({"stubs": ["moyenne.py"], "command": "python3 test_moyenne.py"})

# Exercice 2

Un carré magique est un carré composé de nombres dont les sommes des nombres de chaque ligne, 
les sommes des nombres de chaque colonne et les sommes des nombres de chaque diagonale principale sont égales

On représente un carré sous la forme d'une liste de listes de nombres.

```python
carre3 = [
    [2, 7, 3],
    [9, 5, 1],
    [4, 3, 8]
]

carre4 = [
    [4, 5, 11, 14],
    [15, 10, 8, 1],
    [6, 3, 13, 12],
    [9, 16, 2, 7]
]
```

?[Quelle est la valeur de len(carre4) ?]
-[ ] 1
-[ ] 3
-[X] 4
-[ ] 16

?[Quelle est la valeur de carre3[1] ?]
-[ ] 2
-[ ] 7
-[ ] 9
-[ ] [2, 7, 3]
-[X] [9, 5, 1]

?[Quelle est la valeur de carre3[0][2] ?]
-[ ] 7
-[X] 3
-[ ] [2, 7, 3]
-[ ] Cela renvoie une erreur

?[Quelle instruction permet de récupérer la valeur 3 de carre4 ?]
-[ ] carre4[3]
-[ ] carre4[9]
-[X] carre4[2][1]
-[ ] carre4[3][2]

On propose le code suivant:
```python
def somme_ligne(carre, n):
    """
    carre est une liste de listes de nombres
    n est un nombre entier
    """
    somme = 0
    for nombre in carre[n]:
        somme = somme + nombre
    return somme
```

Que vaut somme_ligne(carre4, 2) ? À quoi sert cette fonction ?

Dans l'environnement Python suivant:
1. Définissez la fonction `lignes_magiques` qui prend un carré en paramètre et qui vérifie que les sommes des nombres de chaque ligne sont égales.
1. Définissez la fonction `somme_colonne` qui prend un carré en paramètre, ainsi que le numéro d'une colonne, et qui renvoie la somme des nombres de cette colonne.
1. Définissez la fonction `est_magique` qui prend un carré en paramètre et qui renvoie `True` si le carré est magique et `False` sinon.

@[Carré magique]({"stubs": ["carre_magique.py"], "command": "python3 test_carre_magique.py"})
