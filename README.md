
Pour installer un repo personnalisé (par exemple un dépôt Git contenant des scripts Python) et importer les scripts à l’intérieur, tu peux suivre plusieurs méthodes selon le contexte. Voici les options les plus courantes :

---

### **Méthode 1 : Cloner le repo et ajouter le chemin au `PYTHONPATH`**

1. **Cloner le repo** :
   ```bash
   git clone https://github.com/Dereckt374/utils.git
   ```

2. **Ajouter le dossier au `PYTHONPATH`** :
   Dans ton script Python, ou dans un terminal :
   ```python
   import sys
   sys.path.append('/Git/utils')
   ```

3. **Importer un script** :
   Si ton repo a un fichier `mon_script.py` :
   ```python
   import mon_script
   ```

---

### **Méthode 2 : Utiliser un `setup.py` (repo avec structure de package)**

Si ton repo contient un fichier `setup.py`, tu peux l’installer localement :

1. **Installation en mode "editable"** (recommandé pour le développement) :
   ```bash
   pip install -e /chemin/vers/mon-repo
   ```

2. **Importer les modules dans ton code** :
   Supposons que ton repo a cette structure :
   ```
   mon-repo/
   └── mon_package/
       ├── __init__.py
       └── outils.py
   ```
   Tu peux alors faire :
   ```python
   from mon_package import outils
   ```

---

### **Méthode 3 : Ajouter directement à l’environnement (par exemple avec VSCode ou Jupyter)**

Dans un notebook Jupyter ou dans VSCode, tu peux ajouter dynamiquement le chemin du repo :
```python
import sys
from pathlib import Path

repo_path = Path('/chemin/vers/mon-repo').resolve()
if str(repo_path) not in sys.path:
    sys.path.insert(0, str(repo_path))

# Maintenant tu peux importer
import mon_script
```
---

### ✅ **Structure recommandée du repo**

```
mon-repo/
├── mon_package/             ← ton dossier avec le code (doit contenir __init__.py)
│   ├── __init__.py
│   └── outils.py
├── setup.py
├── pyproject.toml (optionnel, recommandé si moderne)
├── README.md
└── requirements.txt (facultatif)
```

---

### 🛠️ **Fichier `setup.py` minimal**

```python
from setuptools import setup, find_packages

setup(
    name="mon_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # ou ['numpy', 'pandas'] si besoin
)
```

> `find_packages()` cherche tous les dossiers contenant un `__init__.py` dans le repo.

---

### 📦 Installation locale (dev)

Dans le dossier du repo :
```bash
pip install -e .
```

> Le `-e` signifie "editable" : les modifications sont prises en compte sans réinstaller.

---

### 🌐 Installation depuis un repo Git

Tu peux aussi l’installer directement depuis GitHub ou GitLab :

```bash
pip install git+https://github.com/ton-utilisateur/mon-repo.git
```

Ou avec une branche spécifique :
```bash
pip install git+https://github.com/ton-utilisateur/mon-repo.git@dev
```

---

### 📥 Exemple d’import après installation

Si ton fichier `mon_package/outils.py` contient :

```python
def bonjour():
    print("Salut depuis le package !")
```

Tu pourras l’utiliser comme :
```python
from mon_package import outils

outils.bonjour()
```

---

## Authentification

```bash
# 1. Générer une paire de clés SSH (publique/privée)
ssh-keygen -t ed25519 -C "tonmail@example.com"
# => Crée ~/.ssh/id_ed25519 (privée) et ~/.ssh/id_ed25519.pub (publique)

# 2. Copier la clé publique
cat ~/.ssh/id_ed25519.pub
# => Copier le contenu pour le coller dans GitHub

# 3. Ajouter la clé publique à GitHub
# => GitHub > Settings > SSH and GPG keys > New SSH key > Coller la clé

# 4. Tester la connexion
ssh -T git@github.com
# => Vérifie que GitHub te reconnaît via ta clé

# 5. Cloner le dépôt privé via SSH
git clone git@github.com:ton-utilisateur/ton-repo.git
# => Clone sécurisé sans mot de passe

```

> 💡 **Règle d’or** : ne jamais partager `id_ed25519`, ta clé privée. Si elle est compromise, recrée une nouvelle paire.
