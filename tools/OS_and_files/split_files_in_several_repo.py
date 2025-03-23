import os
import shutil

def organiser_fichiers_md(repertoire_source):
    """
    Organise les fichiers .md d'un répertoire source en sous-dossiers contenant chacun 10 fichiers.
    
    :param repertoire_source: Chemin du répertoire contenant les fichiers .md
    """
    # Liste des fichiers .md
    fichiers_md = [f for f in os.listdir(repertoire_source) if f.endswith('.md')]
    
    if not fichiers_md:
        print("Aucun fichier .md trouvé dans le répertoire.")
        return
    
    # Trier les fichiers pour une meilleure organisation (optionnel)
    fichiers_md.sort()
    
    # Découper la liste en paquets de 10 fichiers
    for i in range(0, len(fichiers_md), 10):
        dossier_numero = (i // 10) + 1
        dossier_nom = os.path.join(repertoire_source, f'dossier_{dossier_numero}')
        
        # Créer le dossier s'il n'existe pas
        os.makedirs(dossier_nom, exist_ok=True)
        
        # Déplacer les fichiers dans le dossier
        for fichier in fichiers_md[i:i + 10]:
            chemin_source = os.path.join(repertoire_source, fichier)
            chemin_destination = os.path.join(dossier_nom, fichier)
            shutil.move(chemin_source, chemin_destination)
        
        print(f"{len(fichiers_md[i:i + 10])} fichiers déplacés vers {dossier_nom}")


# Exemple d'utilisation
if __name__ == "__main__":
    # repertoire_source = "chemin/vers/votre/repertoire"  # Remplacez par votre chemin
    repertoire_source = os.getcwd()
    organiser_fichiers_md(repertoire_source)

