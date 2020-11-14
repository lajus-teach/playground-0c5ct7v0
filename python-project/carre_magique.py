def somme_ligne(carre, n):
    """
    carre est une liste de listes de nombres
    n est un nombre entier
    """
    somme = 0
    for nombre in carre[n]:
        somme = somme + nombre
    return somme
    
# À compléter