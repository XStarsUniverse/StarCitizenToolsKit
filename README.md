# StarCitizenToolsKit

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
