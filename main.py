"""Voici le programme relatif aux tuples qui prend en compte deux fonctions secondaires"""


#### Fonctions secondaires
"""Cette fonction se base sur la méthode de l'iteration"""

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    c = [s[0]]
    o = [1]

    k = 1

    while k < len(s):
        if s[k] == s[k-1]:
            o[-1] += 1
        else :
            c.append(s[k])
            o.append(1)
        k += 1
    return list(zip(c,o))

def artcode_r(s):
    """Cette fonction se base sur la méthode de la recursivite"""

    """retourne la liste de tuples encodant une chaîne de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    compt = 1

    while compt < len(s) and s[compt] == s[0]:
        compt += 1
    tuples = (s[0], compt)
    return [tuples] + artcode_r(s[compt:])

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif

#### Fonction principale

"""Ici la fonction principale faita appel aux deux fonctions secondaires"""
def main():
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
