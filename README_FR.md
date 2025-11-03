# ⏸️ GlobalExam Pause - Mode Intelligent

> **Langue :** [🇬🇧 English](README_EN.md) | [🇫🇷 Français](README_FR.md)

<div align="center">

![GlobalExam Pause](assets/endless_pause_logo.png)

**Automatisation intelligente avec pauses personnalisables pour GlobalExam Activité 7**

[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Windows](https://img.shields.io/badge/Windows-0078D4?style=for-the-badge&logo=windows&logoColor=white)](https://www.microsoft.com/)

**Mode Intelligent • Pauses Personnalisables • Chronomètre en Direct**

</div>

---

## 🎯 Qu'est-ce que GlobalExam Pause ?

**GlobalExam Pause** est un outil d'automatisation professionnel avec interface graphique pour l'Activité 7 de GlobalExam avec gestion intelligente des pauses. Parfait pour des schémas d'automatisation plus humains.

### ✨ Fonctionnalités Principales

- ⏸️ **Mode Pause Intelligent** - Pauses personnalisables entre les cycles
- ⏱️ **Chronomètre en Direct** - Affichage temps réel MM:SS
- ⚙️ **Durée Personnalisable** - Choisissez 10, 20, 30, 40, ou 45 minutes (max)
- 📊 **Statistiques Complètes** - Cycles, questions répondues, temps total
- 🎨 **Interface Moderne** - Thème sombre élégant avec accents verts
- 🔐 **Protection par Mot de Passe** - Authentification sécurisée au premier lancement
- 📐 **Adaptation Automatique** - Fonctionne sur toutes les résolutions
- ⏭️ **Ignorer la Pause** - Bouton de remplacement manuel

---

## 📦 Installation

### Démarrage Rapide

1. **Cloner ou télécharger** ce dépôt
2. **Installer les dépendances :**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Lancer l'application :**
   ```powershell
   python endless_final_pause_GUI.py
   ```

### Prérequis

- **OS :** Windows 10/11
- **Python :** 3.13+ (ou Python 3.x)
- **Navigateur :** Chrome/Firefox à 100% de zoom
- **Écran :** Toute résolution (adaptation automatique)

---

## 🚀 Utilisation

### Lancer l'Application

```powershell
python endless_final_pause_GUI.py
```

### Premier Lancement

Au premier démarrage, un code d'accès vous sera demandé :
- Entrez le code lorsqu'il est demandé (saisie masquée)
- Un fichier `.first_run_ok` est créé après authentification
- Le code ne sera plus demandé sauf si vous supprimez ce fichier

### Utiliser l'Application

1. Ouvrez l'Activité 7 de GlobalExam dans votre navigateur
2. **Sélectionnez la durée de pause** (10-45 minutes)
3. Cliquez sur **DÉMARRER** dans l'application
4. L'application va :
   - Détecter votre résolution d'écran
   - Normaliser le zoom du navigateur à 100%
   - Traiter les questions 1-6
   - **Démarrer la pause personnalisable**
   - Traiter les questions 7-13
   - Répéter le cycle
5. Cliquez sur **IGNORER PAUSE** pour sauter la pause
6. Cliquez sur **ARRÊTER** pour stopper à tout moment

---

## ⏱️ Fonctionnalités du Chronomètre

### Compte à Rebours en Temps Réel

Le chronomètre affiche :
- **Format :** MM:SS (ex: 40:00, 15:30, 00:45)
- **Mise à jour :** Chaque seconde
- **Code couleur :**
  - 🟢 **Vert** quand > 5 minutes restantes
  - 🟠 **Orange** quand 1-5 minutes restantes
  - 🔴 **Rouge** quand < 1 minute restante

### Durée Personnalisable

Choisissez la durée de votre pause :
- **10 minutes** - Pause rapide
- **20 minutes** - Pause courte
- **30 minutes** - Pause moyenne
- **40 minutes** - Standard (par défaut)
- **45 minutes** - Maximum autorisé

**Note :** La durée est verrouillée pendant l'exécution. Pause maximum : 45 minutes.

---

## 📊 Suivi des Statistiques

### Ce qui est Suivi

| Statistique | Description |
|-------------|-------------|
| **🔄 Cycles** | Total des cycles complétés |
| **❓ Questions** | Total des questions répondues (13 par cycle) |
| **⏱️ Temps** | Durée de la session (HH:MM:SS) |
| **État** | Statut actuel (En cours/Arrêté/En pause) |

---

## 📂 Structure du Projet

```
GlobalExam_Pause/
├── endless_final_pause_GUI.py  # Application principale
├── final_test.py               # Fonctions auxiliaires
├── PNJ/                        # Modèles d'images
├── assets/                     # Logos et icônes
│   ├── endless_pause_logo.png
│   └── endless_pause_logo.ico
├── requirements.txt            # Dépendances Python
├── .gitignore                 # Règles d'exclusion Git
├── LICENSE                     # Fichier de licence
└── README.md                   # Ce fichier
```

---

## ⚙️ Configuration

### Adaptation Automatique de la Résolution

Adapte automatiquement les coordonnées :
- Référence : 1920x1080
- Ajuste à votre écran
- Aucune configuration manuelle nécessaire

### Normalisation du Zoom du Navigateur

Au démarrage :
- Appuie sur `Ctrl+0` trois fois
- S'assure du zoom à 100%
- Prévient les clics ratés

---

## 🐛 Dépannage

| Problème | Solution |
|----------|----------|
| **Le chrono ne compte pas** | La pause n'a pas encore commencé (après Q6) |
| **Questions sautées** | Vérifiez que le zoom est à 100% |
| **Impossible de changer la durée** | Arrêtez d'abord l'automatisation |
| **Stats ne se mettent pas à jour** | Vérifiez que l'automatisation fonctionne |

---

## ⚠️ Notes Importantes

- ✅ **Position de la Pause :** Après Question 6, avant Question 7
- ✅ **Verrouillage Durée :** Impossible de changer pendant l'exécution
- ✅ **Durée Maximum :** 45 minutes
- ✅ **Ignorer Disponible :** Cliquez "IGNORER PAUSE" à tout moment
- ⚠️ **Zoom Navigateur :** Doit rester à 100%

---

## 💡 Conseils et Bonnes Pratiques

### Choisir la Durée de Pause

- **10-20 min :** Tests rapides ou sessions courtes
- **30-40 min :** Usage standard (imite les pauses humaines)
- **45 min :** Durée maximum autorisée

---

## 📝 Licence

Ce projet est fourni à des fins d'automatisation personnelle/éducative. Veuillez respecter les conditions d'utilisation de la plateforme.

---

<div align="center">

**Fait avec ❤️ pour l'automatisation GlobalExam**

⏸️ **GlobalExam Pause** - Mode Intelligent

</div>
