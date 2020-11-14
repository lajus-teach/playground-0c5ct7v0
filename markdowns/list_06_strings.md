# Les listes et les chaînes de caractères

Les méthodes `split()` et `join()` sont très utilisées pour la manipulation des chaînes de caractères.

`split()` permet notamment de décomposer un phrase en une liste de mots et inversement `join()` permet de mettre bout à bout une liste de mots.

```python runnable
texte = "Bonjour le monde !"
mots = texte.split()
print(mots)
texte = " ".join(mots)
print(texte)
```

Je vous conseille vivement de faire un tour sur la [documentation de split](#https://www.w3schools.com/python/ref_string_split.asp) et [de join](#https://www.w3schools.com/python/ref_string_join.asp)
pour avoir une description détaillée.

# Exercices

Quand Yoda parle à quelqu'un il doit toujours utiliser plus de 2 mots. Compléter la fonction `word_count()` pour qu'elle renvoie le nombre de mots dans 
la phrase passée en paramètre.

@[Much to learn, you still have]({"stubs": ["wordcount.py"], "command": "python3 test_wordcount.py"})

Parler comme Yoda tu veux. Pour cela compléter la fonction `yodaification()` tu devras. 
De la phrase passée en argument, les deux premiers mots à la fin de la phrase tu déplaceras. Une nouvelle phrase ainsi créée tu renverras.

@[Much to learn, you still have]({"stubs": ["yoda.py"], "command": "python3 test_yodaification.py"})

