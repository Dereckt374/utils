import os
def cherchefichier(fichier, rep):
 
    # recherche du contenu du répertoire rep (fichiers et sous-répertoires)
    entrees = os.listdir(rep)
 
    # traitement des fichiers du répertoire
    for entree in entrees:
        if (not os.path.isdir(os.path.join(rep, entree))) and (entree==fichier):
            return rep
 
    # traitement récursif des sous-répertoires de rep
    for entree in entrees:
        rep2 = os.path.join(rep, entree)
        if os.path.isdir(rep2):
            chemin = cherchefichier(fichier, rep2)
            if chemin!="":
                return chemin
 
    # si pas trouvé, renvoie une chaine vide
    return ""