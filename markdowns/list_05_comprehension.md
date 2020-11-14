# Construction d'une liste par compréhension

On peut construire une liste de trois manière différentes:
1. en énumérant chaque élément,
1. de manière itérative,
1. par comprehension.

```python runnable
# Enumération
l = [0, 1, 4, 9, 16]
print(l)
# Construction itérative
l = []
for i in range(5):
    l.append(i*i)
print(l)
# Par compréhension
l = [ i*i for i in range(5) ]
print(l)
```
On peut lire cette dernière instruction de la manière suivante: `l` est la liste des valeurs `i*i` pour `i` allant de 0 à 5.

**QCM**

```python
l1 = [ i for i in range(5)]
l2 = [ i+2 for i in range(5)]
l3 = [ c for c in "Hello"]
l4 = [ c.upper() for c in "Hello"]
```

?[Que vaut l1 ?]
-[X] [0, 1, 2, 3, 4]
-[ ] [1, 2, 3, 4, 5]
-[ ] [2, 3, 4, 5, 6]
-[ ] [1, 2, 3, 4]

?[Que vaut l2 ?]
-[ ] [0, 1, 2, 3, 4]
-[ ] [1, 2, 3, 4, 5]
-[X] [2, 3, 4, 5, 6]
-[ ] [3, 4, 5, 6, 7]
-[ ] [3, 4, 5, 6]

?[Que vaut l3 ?]
-[ ] "Hello"
-[ ] "H" "e" "l" "l" "o"
-[ ] [ "Hello" ]
-[X] [ "H", "e", "l", "l", "o" ]

?[Que vaut l4 ?]
-[ ] "Hello"
-[ ] "HELLO"
-[ ] [ "Hello" ]
-[ ] [ "HELLO" ]
-[ ] [ "H", "e", "l", "l", "o" ]
-[X] [ "H", "E", "L", "L", "O" ]

---

On peut utiliser plusieurs variables dans la construction par compréhension:

```python runnable
l = [ i+j for i in range(5) for j in range(3) ]
print(l)
# Est équivalent à la construction itérative:
l = []
for i in range(5):
    for j in range(3):
        l.append(i+j)
print(l)
```

**QCM**

```python
l5 = [ i for j in range(2) for i in range(3, 5)]
l6 = [ i for i in range(3, 5) for j in range(2)]
l7 = [ (i, j) for i in range(2) for j in range(2)]
```
?[Que vaut l5 ?]
-[ ] [1, 2, 3, 4]
-[ ] [1, 2, 1, 2]
-[ ] [1, 1, 2, 2]
-[ ] [3, 4]
-[X] [3, 4, 3, 4]
-[ ] [3, 3, 4, 4]

?[Que vaut l6 ?]
-[ ] [1, 2, 3, 4]
-[ ] [1, 2, 1, 2]
-[ ] [1, 1, 2, 2]
-[ ] [3, 4]
-[ ] [3, 4, 3, 4]
-[X] [3, 3, 4, 4]

?[Que vaut l7 ?]
-[ ] [0, 1, 0, 1]
-[ ] [0, 0, 0, 1, 1, 0, 1, 1]
-[ ] [0, 0, 1, 0, 0, 1, 1, 1]
-[X] [(0, 0), (0, 1), (1, 0), (1, 1)]
-[ ] [(0, 0), (1, 0), (0, 1), (1, 1)]

---

On peut utiliser le mot-clé `if` pour filtrer des éléments de la liste:

```python runnable
# On construit la liste de 0 à 20 en enlevant chaque multiple de 3:
l = [ i for i in range(21) if i % 3 != 0 ]
print(l)
# Est équivalent à la construction itérative:
l = []
for i in range(21):
    if i % 3 != 0:
        l.append(i)
print(l)
```

**QCM**

```python
liste = [ -5, 2, 3, -7, -2, 4, 2, 0, 16]
l8 = [ i for i in liste if i > 0]
l9 = [ i for i in liste if i*i in liste]
```

?[Que vaut l8 ?]
-[ ] [-5, -7, -2]
-[ ] [2, 3, 4, 2, 0, 16]
-[X] [2, 3, 4, 2, 16]
-[ ] [2, 3, 4, 16]

?[Que vaut l9 ?]
-[ ] [-5, 3, -7]
-[ ] [2, 4, 2]
-[ ] [2, 4, 2, 16]
-[ ] [2, 4, 2, 0]
-[ ] [2, -2, 4, 2]
-[ ] [2, -2, 4, 2, 16]
-[X] [2, -2, 4, 2, 0]

# Exercice

Yoda dispose de la liste des couples maître/padawan du temple (une liste de tuples de taille 2). Il souhaite que vous complétiez la fonction `inverse_couple` 
renvoyant une nouvelle liste contenant les couples padawan/maître du temple.

@[Much to learn, you still have]({"stubs": ["inverse.py"], "command": "python3 test_inverse.py"})