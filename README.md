# StarCitizenToolsKit

🔗 **Languages / Langues** :

* [🇫🇷 Français](#-présentation-générale)
* [🇬🇧 English](#-overview)

## 🌌 Présentation générale

**StarCitizenToolsKit** est un dépôt central du projet **XStars Universe**, un fan project dédié à l’écosystème de données du jeu **Star Citizen**.

Ce dépôt a deux objectifs principaux :

1. **Stocker et versionner les données JSON extraites du jeu** (LIVE / PTU / HOTFIX)
2. **Fournir un ensemble d’outils (ToolsKit)** permettant de générer, mettre à jour et maintenir ces données localement

Ces données sont utilisées comme **référence officielle de version** au sein de l’écosystème **XStars Universe**, notamment pour notre **API** (en cours de développement).

---

## 📁 Structure du dépôt

À la racine du dépôt, on trouve la structure suivante :

```
StarCitizenToolsKit/
├─ LIVE/
├─ PTU/
├─ HOTFIX/
├─ ToolsKit/
└─ README.md
```

---

## 📦 Dossiers de données (LIVE / PTU / HOTFIX)

### 🎯 Rôle

Les dossiers `LIVE/`, `PTU/` et `HOTFIX/` contiennent les **données JSON générées à partir des fichiers du jeu Star Citizen**.

Ces données sont extraites automatiquement à l’aide des outils présents dans `ToolsKit/`.

---

### 📄 Fichier `version`

Chaque dossier (`LIVE`, `PTU`, `HOTFIX`) contient un fichier nommé :

```
version
```

Ce fichier permet d’identifier **de manière fiable la version réelle des données**, indépendamment :

* du nom des commits Git
* du format des versions CIG

Exemple de version côté jeu :

```
4.5.0-ptu.10938459
```

Chez **XStars Universe**, ce fichier `version` est utilisé comme **source de vérité** pour :

* le versioning des datasets
* la cohérence des données exposées via l’API
* les traitements backend

---

## 🛠️ ToolsKit/

Le dossier `ToolsKit/` contient **l’ensemble des scripts et outils techniques** permettant :

* l’extraction des données depuis les fichiers du jeu
* la transformation et le nettoyage des données
* la génération des dossiers `LIVE/`, `PTU/`, `HOTFIX/`

On y retrouve notamment :

* des scripts Python d’orchestration
* des scripts `.bat` générés automatiquement
* l’intégration de ScDataDumper et unp4k

👉 Un **README dédié** est présent dans ce dossier et explique en détail :

* l’installation
* la configuration
* l’usage des outils

---

## 🔗 Liens et dépendances externes

Ce projet s’appuie sur des outils open-source tiers :

### 📦 ScDataDumper

* Projet : [https://github.com/octfx/ScDataDumper](https://github.com/octfx/ScDataDumper)
* Utilisé pour : extraction et structuration des données Star Citizen
* Licence et droits : voir le dépôt officiel

### 📦 unp4k

* Projet : [https://github.com/dolkensp/unp4k/](https://github.com/dolkensp/unp4k/)
* Utilisé pour : extraction des fichiers depuis les archives `.p4k`
* Licence et droits : voir le dépôt officiel

---

## ✍️ Scripts XStars Universe

Les **scripts Python**, les scripts d’orchestration et la logique d’automatisation présents dans ce dépôt sont :

> © **XStars Universe**

Ils ont été développés spécifiquement pour :

* répondre aux besoins de notre fan site
* garantir un versioning fiable des données
* préparer l’exposition des données via une **API publique** (à venir)

---

## 🚀 API XStars Universe (à venir)

Les données présentes dans ce dépôt seront prochainement accessibles via une **API en ligne XStars Universe**, permettant :

* la consultation des données Star Citizen
* l’exploitation par des outils tiers
* la création de visualisations et services communautaires

---

## ⚠️ Disclaimer

* **Star Citizen** est une marque déposée de **Cloud Imperium Games**.
* **XStars Universe** est un **fan project**, non affilié à Cloud Imperium Games.
* Ce dépôt est destiné à un usage communautaire et technique.

---

© XStars Universe — Fan project Star Citizen

---

# 🇬🇧 Overview

## 🌌 General presentation

**StarCitizenToolsKit** is a central repository of the **XStars Universe** project, a fan-driven initiative dedicated to the **Star Citizen** data ecosystem.

This repository has two main goals:

1. **Store and version JSON data extracted from the game** (LIVE / PTU / HOTFIX)
2. **Provide a complete ToolsKit** to locally generate, update, and maintain these datasets

These datasets are used as the **official version reference** within the **XStars Universe** ecosystem, especially for our upcoming **public API**.

---

## 📁 Repository structure

```
StarCitizenToolsKit/
├─ LIVE/
├─ PTU/
├─ HOTFIX/
├─ ToolsKit/
└─ README.md
```

---

## 📦 Data folders (LIVE / PTU / HOTFIX)

### 🎯 Purpose

The `LIVE/`, `PTU/`, and `HOTFIX/` directories contain **JSON data generated from Star Citizen game files**.

This data is automatically produced using the tools located in `ToolsKit/`.

---

### 📄 `version` file

Each data folder contains a file named:

```
version
```

This file provides a **reliable identification of the actual game data version**, regardless of:

* Git commit naming
* CIG version formatting

Example game version:

```
4.5.0-ptu.10938459
```

At **XStars Universe**, this `version` file is used as the **single source of truth** for:

* dataset versioning
* API consistency
* backend processing

---

## 🛠️ ToolsKit/

The `ToolsKit/` directory contains all **technical tools and scripts** required to:

* extract data from Star Citizen game files
* process and clean datasets
* generate the `LIVE/`, `PTU/`, and `HOTFIX/` directories

It includes:

* Python orchestration scripts
* auto-generated `.bat` scripts
* integrations with ScDataDumper and unp4k

👉 A dedicated **README** is available inside this directory explaining installation, configuration, and usage.

---

## 🔗 External dependencies

This project relies on the following open-source tools:

### 📦 ScDataDumper

* Project: [https://github.com/octfx/ScDataDumper](https://github.com/octfx/ScDataDumper)
* Usage: Star Citizen data extraction and structuring
* License and rights: see the official repository

### 📦 unp4k

* Project: [https://github.com/dolkensp/unp4k/](https://github.com/dolkensp/unp4k/)
* Usage: extraction of files from `.p4k` archives
* License and rights: see the official repository

---

## ✍️ XStars Universe scripts

All **Python scripts, orchestration logic, and automation** contained in this repository are:

> © **XStars Universe**

They are developed specifically to:

* support our fan site needs
* ensure reliable dataset versioning
* prepare data exposure through a **public API** (coming soon)

---

## 🚀 XStars Universe API (coming soon)

The datasets hosted in this repository will soon be accessible through the **XStars Universe online API**, allowing:

* data querying
* third-party integrations
* community-driven tools and visualizations

---

## ⚠️ Disclaimer

* **Star Citizen** is a registered trademark of **Cloud Imperium Games**.
* **XStars Universe** is a **fan project**, not affiliated with Cloud Imperium Games.
* This repository is intended for technical and community use only.

---

© XStars Universe — Fan project Star Citizen
