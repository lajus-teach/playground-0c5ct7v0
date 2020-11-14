# Les chaînes de caractères

Une chaîne de caractères est un objet Python pouvant contenir 0, 1 ou plusieurs caractères.

En Python, toute valeur comprise entre deux guillemets doubles `"` ou deux guillemets simples `'` est considérée comme du texte:

```python runnable
# Il faut bien distinguer la varible hello de la chaîne de caractère "hello"
hello = "hello"
hello = "world"
world = hello
print(hello)
print(world)
```

Ou toute valeur comprise entre deux triple guillemets doubles `"` ou deux triple guillemets simples `'`:
```python runnable
guillements_simples = "C'est simple"
print(guillemets_simples)
guillemets_doubles = 'Il me dit: "Bonjour".'
print(guillemets_double)
triple_guillemets = """Les triples guillemets sont utiles pour:
 - écrire du texte sur plusieurs lignes,
 - écrire du texte contenant à la fois des guillemets simples ' et des guillemets doubles ".
"""
print(triple_guillemets)
```

# Opérations sur les chaînes de caractères

## Opérations sur les listes:

Les chaînes de caractères sont des listes de caractères, on peut donc les manipuler comme telles:
 * **Taille**: à l'aide de la fonction `len()`.
 * **Concaténation**: à l'aide de l'opération `+`.
 * **Appartenance**: le mot-clé `in`, à l'extérieur d'une boucle `for`, teste l'appartenance.
 * **Itération**: le mot-clé `in`, à l'intérieur d'une boucle `for`, permet d'itérer sur les lettres d'une chaîne de caractère.
 * **Accès** à la ième lettre à l'aide de l'opérateur `[i]`:
 * **Sous-chaîne** de la ième lettre (incluse) à la jième lettre (excluse) à l'aide de l'opération `[i:j]`.

```python runnable
t1 = "hello world"
t2 = "we are the world"
print(len(t1), len(t2))
print(t2 + t1)
print(t1[0] + t2[3] + t2[-1])
print(t1[:5] + t2[6:])
print(t1[5:] in t2)
```

## QCM

```python
a = "hello"
b = 'world'
```

Cochez la/les bonne(s) réponse(s):

?[Que vaut a + b ?]
-[ ] "hello"'world'
-[ ] hello world
-[ ] "hello world"
-[ ] 'hello world'
-[ ] helloworld
-[X] "helloworld"
-[X] 'helloworld'

?[Que vaut a[1] ?]
-[ ] h
-[ ] "h"
-[ ] e
-[X] "e"
-[ ] b

?[Que vaut b[1:4] ?]
-[X] "orl"
-[ ] "orld"
-[ ] "wor"
-[ ] "worl"

## Quelques méthodes

Une *méthode* est une *fonction* qu'on peut appliquer à un objet Python d'un certain type. En Python, pour chaque type d'objet, un ensemble de méthodes
permettant de manipuler ce type d'objet est déjà prédéfini.

La syntaxe d'appel à une méthode est légèrement différente de la syntaxe d'appel à une fonction. Elle a la forme: `objet.methode(arguments)`

Par exemple, Python prédéfini un ensemble de méthodes permettant de manipuler spécifiquement les chaînes de caractères. 

Une liste exhaustive des méthodes permettant de manipuler des chaînes de caractères en Python peut être retrouvée [ici](#https://www.w3schools.com/python/python_ref_string.asp).

On en présente quelque unes:
 * La méthode `upper()` (resp. `lower()`) renvoie la chaîne mise en majuscules (resp. minuscules):
```python runnable
# Bien noté la syntaxe particulière de l'appel à la méthode upper()
t1 = "baba".upper()
t2 = "Hello WORLD!".upper()
t3 = "Hello WORLD!".lower()
print(t1)
print(t2)
print(t3)
```
 * La méthode `replace(from, to)` prend deux arguments et remplace dans la chaîne objet, chaque occurence de la chaîne passée en premier argument, par la chaîne passée en second:
```python runnable
t1 = "baba".replace("b", "d")
t2 = "baba".replace("a", "")
t3 = "tttt".replace("tt", "t")
print(t1)
print(t2)
print(t3)
```

# Construction de chaînes

En Python, une chaîne de caractères ne peut pas être modifiée (immutable):
```python runnable
t = "abc"
t[0] = "b"
print("t vaut:", t)
```

Les opérations sur les listes ne modifient pas la chaîne mais renvoie une nouvelle chaîne:
```python runnable
t1 = "abc"
t2 = "b" + t1[1:]
# Ici t2 contiendra "bbc" mais t1 contiendra toujours "abc", t1 n'est pas modifié.
t3 = t1[0] + "bb"
print(t1, t2, t3)
```

Les méthodes ne modifient pas la chaîne mais renvoie une nouvelle chaîne:
```python runnable
t1 = "baba"
t2 = t1.replace("b", "d")
# Ici t2 contiendra "dada" mais t1 contiendra toujours "baba", t1 n'est pas modifié.
t3 = t1.replace("a", "o")
print(t1, t2, t3)
```

Donc comment faire pour transformer une chaîne de caractères ?

## Méthode 1: en manipulant la chaîne de caractères.

Cette approche fonctionne pour les manipulations simples.

Par exemple pour construire la chaîne contenant les `n` premières lettres de l'alphabet, on peut construire la chaîne contenant tout l'alphabet et
renvoyer les n premiers caractères:

```python runnable
def alphabet(n):
    a = "abcdefghijklmnopqrstuvwxyz"
    return a[:n]

print(alphabet(3))
print(alphabet(18))
```

## Méthode 2: en construisant, caractère par caractère la chaîne transformée.

Pour les manipulations plus complexes il est souvent plus facile de travailler caractères par caractères.

Sur le même exemple:
```python runnable
def alphabet(n):
    a = "abcdefghijklmnopqrstuvwxyz"
    # On initialise une variable dans laquelle on va stocker le résultat:
    resultat = ""
    for i in range(n):
        # On calcule le prochain caractère à ajouter:
        caractere_a_ajouter = a[i]
        # Ici c'est assez simple, c'est seulement la ieme lettre de l'alphabet.
        # Mais le calcul peut être plus compliqué pour des manipulations plus
        # complexes.
        #
        # Enfin, on ajoute ce caractère au résultat:
        resultat = resultat + caractere_a_ajouter
    return resultat

print(alphabet(3))
print(alphabet(18))
```

En utilisant cette structure (qui est très générale):
 1. On n'a plus besoin de manipuler la liste dans sa globalité,
 1. On a juste à transformer chaque caractère indépendamment les uns des autres.

# Exercice d'application

On demande à Bob d'écrire la fonction `swapcase()` prenant en argument une chaîne de caractère et inversant la casse de chaque caractère de cette chaîne.

Cela signifie que cette fonction devra renvoyer la chaîne de caractères avec toutes les minuscules mises en majuscules et toutes les majuscules mises en minuscules (la ponctuation
restant inchangée).

## Méthode 1: en manipulant la chaîne de caractère.

Bob vous propose différentes solutions que vous allez étudier:

**Proposition 1**: en utilisant les méthodes `upper()` et `lower()`:

```python runnable
# Proposition 1
def swapcase(texte):
    # On passe les minuscules en majuscules:
    texte.upper()
    # Et les majuscules en minuscules:
    texte.lower()
    # Et on renvoie ce résultat:
    return texte
```

Tester cette fonction. *Quel est le problème ? Expliquez*

---

**Proposition 2**:

```python runnable
# Proposition 2
def swapcase(texte):
    # On passe les minuscules en majuscules:
    t1 = texte.upper()
    # Et les majuscules en minuscules:
    t2 = t1.lower()
    # Et on renvoie ce résultat:
    return t2
```

Tester cette fonction. *Quel est le problème ? Expliquez*

---

**Proposition 3**: en utilisant la méthode `replace()`:

```python runnable
# Proposition 2
def swapcase(texte):
    t = texte
    t = t.replace("a", "A")
    t = t.replace("b", "B")
    # ...
    return t
```

?[En tout, combien de fois faut-il appeler la méthode replace() pour que swapcase() fonctionne ?]
-[ ] 2
-[ ] 26
-[X] 52
-[ ] Autant de fois qu'il y a de caractères dans la variable texte.


## Méthode 2: en construisant, caractère par caractère la chaîne transformée.

Bob décide finalement de transformer la chaîne, caractère par caractère. Il arrive à trouver une solution.
Cette solution utilise notamment les méthodes `isupper()` et `islower()`. Vous pouvez vous référer à [la documentation](#https://www.w3schools.com/python/python_ref_string.asp)
pour comprendre le fonctionnement de ces méthodes.

Néanmoins, lors de sa soumission, les lignes du programme ont étaient mélangées. À vous de les remettre dans le bon ordre.

---

**Explication sur l'interface exercices**: Dans cette interface exercice, vous devez juste définir correctement la fonction swapcase(). 

**Important**, lorsque vous appuyer sur RUN, cela lance
un *autre* script Python que j'ai créé, dont vous n'avez pas accès, qui va effectuer des tests unitaires sur votre fonction.

Si tous les tests unitaires que j'ai créé fonctionnent, l'interface vous indiquera SUCCESS.
Sinon, elle vous renverra un message d'erreur avec éventuellement une description du test unitaire ayant échoué.

---

@[Remettre dans le bon ordre.]({"stubs": ["swapcase.py"], "command": "python3 test_swapcase.py"})

