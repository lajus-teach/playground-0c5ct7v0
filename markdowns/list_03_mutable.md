# Mutable et Immutable

La différence majeure entre un *tuple* et une *liste* est que:
 * Un tuple **ne peut pas être modifié** (**immutable**)
 * Une liste **peut être modifiée** (**mutable**)

On peut modifier les **valeurs des éléments**:
```python runnable
x = [1, 2, 3, 5]
x[3] = 4
print(x)
```

Mais on peut aussi modifier la **structure de la liste**:
```python runnable
x = [1, 2, 3, 5]
# Ajout de la valeur 6 à la fin de la liste
x.append(6)
print(x)
# Suppresion de l'élément d'indice 0
del x[0]
print(x)
```

# Les références et ses conséquences

**Attention**: Les listes sont stockées *par référence*. C'est-à-dire que lorsque l'on stocke une liste dans une variable, 
on ne stocke pas la liste elle-même mais une référence vers cette liste (l'adresse mémoire où est stockée cette liste).

```python runnable
x = [1, 2, 3, 5]
y = x
x.append(6)
print(x)
print(y)
```

Dans cet exemple, les variables  `x` et `y` contiennent une *référence* vers une *même* liste (`[1, 2, 3, 5]`). Lorsque cette liste est modifiée,
la valeur de `x` **et** de `y` est modifiée.

---

```python runnable
x = [1, 2, 3, 5]
y = x
x = x + [6]
print(x)
print(y)
```

Dans cet exemple l'opération `x + [6]` renvoie une *nouvelle* liste contenant `[1, 2, 3, 5, 6]` mais ne modifie pas la liste anciennement 
référencée par `x` (`[1, 2, 3, 5]`). La valeur de `y` ne change donc pas.

---

```python runnable
x = [1, 2, 3, 5]
y = x[:]
x.append(6)
print(x)
print(y)
```

Dans cet exemple, l'opération `x[:]` (sous-liste) renvoie une copie de la liste `[1, 2, 3, 5]`. Donc ici, `x` continent une référence vers
une liste `[1, 2, 3, 5]` et `y` contient une référence vers une autre liste, qui est une copie de cette liste. `x` et `y` ne référençant pas la
même liste, la modification d'une liste n'entraîne pas la modification de l'autre liste.

# Exercice

Une année s'est écoulée et la nouvelle édition de la course de module de Tatooine est encore plus captivante. 
Cette année, la position de chaque concurrent est stockée dans une liste. 

Parmi les moments phares ce cette édition, il y a:
1. Une panne moteur fait passer le premier concurrent à la dernière position.
2. Le second concurrent accélère et prend la tête de la course.
3. Le dernier concurrent sauve l'honneur et dépasse l'anvant dernier module de la course.
4. Un tir de blaster élimine le module en tête de la course.
5. Dans un spectaculaire retournement de situation, un module qu'on pensait éliminé fait son grand retour à la dernière position.

Compléter la fonction `panne_moteur`, modifiant la liste passée en argument de manière à ce que le premier module passe dernier, le deuxième premier et ainsi de suite.

Compléter la fonction `passe_en_tete`, modifiant la liste passée en argument de manière à ce que le premier module passe deuxième et le deuxième premier.

Compléter la fonction `sauve_honneur`, modifiant la liste passée en argument de manière à ce que le dernier module passe avant-dernier et l'avant-dernier dernier.

Compléter la fonction `tir_blaster`, enlevant le premier concurrent de la liste passée en argument.

Compléter la fonction `retour_inatendu`, ajoutant un concurrent à la fin de la liste passée en argument.

@[Looks like a few Tusken Raiders have camped out on the canyon dune turn!]({"stubs": ["permutation_list.py"], "command": "python3 test_permutation_list.py"})
