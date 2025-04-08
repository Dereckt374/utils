import os
import re

def search_pattern_in_txt_files(directory: str, pattern: str):
    result = []
    regex = re.compile(pattern)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if regex.search(line):
                                result.append((path, line.strip()))
                                break  # On ne prend qu’un exemple par fichier
                except Exception as e:
                    print(f"[Erreur] Impossible de lire {path}: {e}")

    return result

# Exemple d’utilisation
if __name__ == "__main__":
    directory = "/home/vmesle/Nextcloud/ROBUSTA-1U/ROBUSTA-1E_ENSO/ENSO-DATA/ENSO-DATA-IO/0_Pass Report"
    pattern = r"reset"  # Exemple : r"\bERREUR\b"

    matches = search_pattern_in_txt_files(directory, pattern)

    for filepath, example_line in matches:
        print(f"Match trouvé dans : {filepath}")
        print(f"Exemple : {example_line}")
        print("-" * 80)
