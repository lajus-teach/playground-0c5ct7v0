# Assignations multiples

Les tuples peuvent être utilisés pour assigner une valeur à de multiples variables en même temps:

```python runnable
a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
```

On peut les utiliser pour effectuer des opérations en simultané.

```python runnable
a, b = 3, 5
a, b = a + b, a * b
print(a, b)
```

```python runnable
a, b = 3, 5
a = a + b
b = a * b
print(a, b)
```

Dans le premier code, les valeurs `a + b` et `a * b` sont calculées indépendemment en considérant les valeurs précédentes de `a` (3) et de `b` (5). 
Dans le deuxième code on calcule d'abord la nouvelle valeur de `a` (3 + 5 = 8), puis la nouvelle valeur de `b` (8 * 5 = 40).

Tentez d'abord de répondre au QCM avant d'exécuter ce bloc de code:
```python runnable
a = 12
b = 14
a, b = b, a
print(a, b)
```

?[Qu'affiche le code précédent ?]
-[ ] a, b
-[ ] 12, 14
-[X] 14, 12
-[ ] 14, 14
-[ ] 12, 12

---

On peut utiliser ces assignations multiples pour rapidement décomposer un tuple:

```python runnable
t = 3, 5
a, b = t
print(a*b)
```

Ou même une liste de tuple:
```python runnable
l = [(3,5), (2,6), (8, 4)]
for a, b in l:
    print(a*b)
```

# Exercice

La fameuse course de module de Tatooine bat son plein et trois concurrents sont en course. La position de chaque concurrent est stockée
dans un tuple de taille 3, mais la course est mouvementée:
1. A cause d'une panne moteur le premier concurrent passe à la dernière position.
2. Le second concurrent accélère et prend la tête de la course.
3. Le dernier concurrent sauve l'honneur et dépasse le second module sur la ligne d'arrivée.

Compléter la fonction `panne_moteur`, prenant en argument un tuple de taille 3, et renvoyant un nouveau tuple où le premier module est 
passé dernier, le second premier et le dernier second.

Compléter la fonction `passe_en_tete`, prenant en argument un tuple de taille 3, et renvoyant un nouveau tuple où le premier module est 
passé second et le second premier.

Compléter la fonction `sauve_honneur`, prenant en argument un tuple de taille 3, et renvoyant un nouveau tuple où le second module est 
passé dernier et le dernier second.

Bonus: Essayer d'écrire la fonction `sauve_honneur` sans manipuler les tuples, mais seulement en faisant appel aux fonctions `panne_moteur` et `passe_en_tete`.

@[Now, this is Podracing! Whoopee!]({"stubs": ["permutation.py"], "command": "python3 test_permutation.py"})
