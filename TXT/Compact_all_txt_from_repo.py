import os

# Chemin du dossier contenant les fichiers txt
dossier ="LOG_TEST_ENDURANCE"

# Nom du fichier de sortie
nom_fichier_sortie = "LOG_TEST_ENDURANCE_DE_05042023_A_25042023.txt"

# Ouvrir le fichier de sortie en mode écriture
with open(nom_fichier_sortie, "w") as f_out:

    # Parcourir tous les fichiers du dossier
    for nom_fichier in os.listdir(dossier):

        # Vérifier si le fichier est un fichier txt
        if nom_fichier.endswith(".txt"):

            # Ouvrir le fichier en mode lecture
            with open(os.path.join(dossier, nom_fichier), "r") as f_in:

                # Lire le contenu du fichier et l'écrire dans le fichier de sortie
                f_out.write(f_in.read())

                # Ajouter une ligne vide à la fin de chaque fichier pour séparer les fichiers
                f_out.write("\n")
