import os
import shutil
import re

os.chdir('/home/vmesle/Documents/Obsidian')

# === Paramètres ===
fichier_log = "/home/vmesle/Téléchargements/log.txt"  # Nom du fichier texte à analyser
pattern = r'\d+-\d+-\d+ \d+:\d+ - Downloading complete\s+(.+)$'  # Expression régulière pour détecter les répertoires

def supprimer_element(chemin):
    """Supprime un fichier ou un répertoire selon le type détecté."""
    if os.path.exists(chemin):
        try:
            if os.path.isdir(chemin):
                shutil.rmtree(chemin)
                print(f"[✔] Répertoire supprimé : {chemin}")
            else:
                os.remove(chemin)
                print(f"[✔] Fichier supprimé : {chemin}")
            return True
        except Exception as e:
            print(f"[✘] Erreur lors de la suppression de '{chemin}' : {e}")
            return False
    else:
        print(f"[!] Chemin introuvable : {chemin}")
        return False

def traitement_fichier(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        lignes = f.readlines()
    # print(lignes)
    for ligne in lignes:
        ligne = ligne.replace("\n", "")
        print(ligne)
        match = re.search(pattern, ligne)
        if match:
            chemin_cible = match.group(1)
            print(f"--> Match trouvé : {chemin_cible}")
            supprimer_element(chemin_cible)

if __name__ == "__main__":
    traitement_fichier(fichier_log)