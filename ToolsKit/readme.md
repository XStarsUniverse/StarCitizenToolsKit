# StarCitizenToolsKit – ToolsKit

---

# 🇫🇷 README – Français

---

## 🌌 À propos du projet XStars Universe

**XStars Universe** est un **fan site communautaire autour de Star Citizen**, actuellement en cours de développement.

Notre objectif est de proposer à la communauté :

* des outils avancés autour des **données du jeu**,
* des visualisations,
* et à terme une **API en ligne** permettant d’exploiter facilement les données de Star Citizen.

Le **ToolsKit** que tu utilises ici est la **première brique technique** de cet écosystème : il permet aux utilisateurs avancés, développeurs et data miners de générer localement les données utilisées par XStars Universe.

À l’avenir, ces mêmes données seront accessibles directement via notre **API en ligne**, sans nécessiter d’installation locale.

## 📌 Présentation

**StarCitizenToolsKit / ToolsKit** est un kit d’outils Windows permettant d’extraire, traiter et exporter les données de Star Citizen (LIVE / PTU / HOTFIX) de manière automatisée.

Le projet repose sur :

* des scripts **Python** (orchestration)
* des scripts **.bat** (outils Star Citizen, Docker, unp4k)
* **Docker Desktop** pour ScDataDumper

Tout est conçu pour être **portable**, compatible GitHub, et sans chemins absolus codés en dur.

---

## 🖥️ Prérequis (obligatoires)

Avant toute utilisation, assure-toi d’avoir installé :

1. **Windows 10 / 11**
2. **Python 3.9+**

   * Téléchargement : [https://www.python.org](https://www.python.org)
   * ⚠️ Cocher **"Add Python to PATH"** à l’installation
3. **Docker Desktop for Windows**

   * Téléchargement : [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
   * Docker doit être lancé au moins une fois
4. **Star Citizen installé** (LIVE / PTU / HOTFIX)

---

## 📁 Structure du dossier

```
StarCitizenToolsKit/
└─ ToolsKit/
   ├─ install.py
   ├─ config.json
   ├─ Dumper.py
   ├─ unp4k/
   └─ ScDataDumper-master/
```

⚠️ Tous les chemins sont **relatifs à `ToolsKit/`**.

---

## ⚙️ Installation (install.py)

### 🔹 Rôle

`install.py` génère automatiquement **tous les fichiers .bat nécessaires** en fonction de la structure du repo et du `config.json`.

Ces fichiers `.bat` **ne doivent pas être commit** (ils sont générés localement).

### 🔹 Comment l’utiliser

1. Ouvre `ToolsKit/`

2. Double-clique sur `install.py`

   **OU** en ligne de commande :

   ```bat
   python install.py
   ```

3. Les fichiers `.bat` sont créés dans :

   * `unp4k/`
   * `ScDataDumper-master/`

---

## 🧩 Configuration (config.json)

### 🔹 Exemple

```json
{
  "starcitizen_install_dir": "C:\\Program Files\\Roberts Space Industries\\StarCitizen",
  "versions": ["LIVE", "PTU", "HOTFIX"],
  "docker_desktop_path": "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
}
```

### 🔹 Paramètres

| Clé                       | Description                                              |
| ------------------------- | -------------------------------------------------------- |
| `starcitizen_install_dir` | Dossier contenant LIVE / PTU / HOTFIX                    |
| `versions`                | Versions supportées (ne pas modifier sauf besoin avancé) |
| `docker_desktop_path`     | Chemin vers Docker Desktop (optionnel si standard)       |

---

## ▶️ Utilisation principale (Dumper.py)

### 🔹 Rôle

`Dumper.py` est le **script principal utilisateur**.
Il orchestre automatiquement :

1. Extraction des données via unp4k
2. Déplacement des fichiers
3. Lancement Docker + ScDataDumper
4. Nettoyage & export final

---

### 🔹 Lancement

#### Méthode simple (recommandée)

👉 **Double-clique sur `Dumper.py`**

Une fenêtre console s’ouvre et affiche :

```
1. LIVE
2. PTU
3. HOTFIX
```

Entre le numéro souhaité puis appuie sur **Entrée**.

---

### 🔹 Ce que fait le script automatiquement

* Vérifie si Docker Desktop est lancé
* Lance Docker si nécessaire
* Attend que le moteur Docker soit prêt
* Exécute les bons `.bat` selon la version choisie
* Arrête proprement en cas d’erreur

Aucune action manuelle requise.

---

## ❗ Points importants

* Les `.bat` sont **générés automatiquement** → ne pas les modifier à la main
* Toujours relancer `install.py` après un `git pull`
* Docker Desktop peut prendre **1 à 3 minutes** au premier lancement

---

## 🧹 Nettoyage Git

Les fichiers `.bat` générés sont ignorés via `.gitignore`.

---

# 🇬🇧 README – English

---

## 🌌 About the XStars Universe project

**XStars Universe** is a **community-driven fan site dedicated to Star Citizen**, currently under active development.

Our goal is to provide the community with:

* advanced **data-driven tools**,
* visualizations,
* and eventually an **online API** to easily consume Star Citizen data.

The **ToolsKit** you are using here is the **first technical building block** of this ecosystem. It allows advanced users, developers, and data miners to locally generate the data used by XStars Universe.

In the future, the same data will be available directly through our **online API**, without requiring any local setup.

## 📌 Overview

**StarCitizenToolsKit / ToolsKit** is a Windows toolchain designed to extract, process and export Star Citizen data (LIVE / PTU / HOTFIX) in a fully automated way.

It relies on:

* **Python scripts** (orchestration)
* **.bat scripts** (Star Citizen tooling)
* **Docker Desktop** for ScDataDumper

Everything is **portable**, GitHub-friendly, and free of hardcoded absolute paths.

---

## 🖥️ Requirements

Before using the toolkit, make sure you have installed:

1. **Windows 10 / 11**
2. **Python 3.9+**

   * Download: [https://www.python.org](https://www.python.org)
   * ⚠️ Enable **"Add Python to PATH"** during installation
3. **Docker Desktop for Windows**

   * Download: [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/)
   * Docker must be started at least once
4. **Star Citizen installed** (LIVE / PTU / HOTFIX)

---

## 📁 Folder structure

```
StarCitizenToolsKit/
└─ ToolsKit/
   ├─ install.py
   ├─ config.json
   ├─ Dumper.py
   ├─ unp4k/
   └─ ScDataDumper-master/
```

All paths are **relative to `ToolsKit/`**.

---

## ⚙️ Installation (install.py)

### 🔹 Purpose

`install.py` automatically generates **all required .bat files** based on the repository structure and `config.json`.

Generated `.bat` files are **local-only** and must not be committed.

### 🔹 How to use

1. Open `ToolsKit/`

2. Double-click `install.py`

   **OR** via command line:

   ```bat
   python install.py
   ```

3. `.bat` files are created inside:

   * `unp4k/`
   * `ScDataDumper-master/`

---

## 🧩 Configuration (config.json)

### 🔹 Example

```json
{
  "starcitizen_install_dir": "C:\\Program Files\\Roberts Space Industries\\StarCitizen",
  "versions": ["LIVE", "PTU", "HOTFIX"],
  "docker_desktop_path": "C:\\Program Files\\Docker\\Docker\\Docker Desktop.exe"
}
```

### 🔹 Settings

| Key                       | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `starcitizen_install_dir` | Folder containing LIVE / PTU / HOTFIX            |
| `versions`                | Supported versions (do not change unless needed) |
| `docker_desktop_path`     | Docker Desktop path (optional if default)        |

---

## ▶️ Main usage (Dumper.py)

### 🔹 Purpose

`Dumper.py` is the **main user-facing script**.
It automatically orchestrates:

1. Data extraction via unp4k
2. File relocation
3. Docker + ScDataDumper execution
4. Final cleanup and export

---

### 🔹 Launching

#### Recommended method

👉 **Double-click `Dumper.py`**

A console window opens and displays:

```
1. LIVE
2. PTU
3. HOTFIX
```

Enter the desired number and press **Enter**.

---

### 🔹 What happens automatically

* Checks if Docker Desktop is running
* Starts Docker if needed
* Waits for Docker engine readiness
* Runs the correct `.bat` files based on the selected version
* Stops safely if an error occurs

No manual intervention required.

---

## ❗ Important notes

* `.bat` files are **auto-generated** → do not edit manually
* Always rerun `install.py` after a `git pull`
* Docker Desktop may take **1–3 minutes** to start on first run

---

## 🧹 Git cleanup

Generated `.bat` files are ignored via `.gitignore`.
