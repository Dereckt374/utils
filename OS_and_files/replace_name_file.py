import os

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        # Vérifie si ':' est présent dans le nom du fichier
        if ':' in filename:
            # Nouveau nom avec ':' remplacé par '.'
            new_filename = filename.replace(':', '.')
            # Chemin complet vers l'ancien et le nouveau fichier
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            # Renommage du fichier
            os.rename(old_file, new_file)
            print(f"Renommé: {old_file} -> {new_file}")

# Chemin du répertoire à modifier
directory_path = '/home/virgil/Nextcloud/ROBUSTA-1U/ROBUSTA-1E_ENSO/Partage Expleo-CSUM pour ENSO/1_Projet/6_Operations/ENSO_photos'

# Appel de la fonction
rename_files_in_directory(directory_path)
