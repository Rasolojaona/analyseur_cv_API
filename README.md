# 🧾 Analyseur de CV avec Groq et FastAPI

🚀 Une API développée avec **FastAPI** qui utilise **Groq API** pour analyser automatiquement des **CV textuels** (support PDF à venir) et retourner une analyse structurée : compétences, expérience, formations, etc.

---

## 📋 Sommaire

- [Fonctionnalités](#rocket-fonctionnalités)
- [Structure du projet](#package-structure-du-projet)
- [Prérequis](#warning-prérequis)
- [Installation & Configuration](#gear-installation--configuration)
- [Lancement du serveur](#play_or_pause-button-lancement)
- [Utilisation de l'API](#electric-plug-utilisation-de-lapi)
- [Exemple de requête/réponse](#mag-exemple-de-requ%C3%AAte-r%C3%A9ponse)
- [À venir / Idées d'évolution](#bulb-%C3%A0-venir)

---

## 🚀 Fonctionnalités

✅ Analyse automatisée de CV via Groq  
✅ Extraction structurée : nom, poste recherché, compétences, expérience professionnelle, formations...  
✅ API REST exposée via FastAPI  
✅ Documentation Swagger intégrée (`/docs`)  
✅ Support texte brut (PDF à venir)

---

## 📦 Structure du projet

```
cv-analyzer/
├── main.py                  # Point d'entrée FastAPI
├── requirements.txt         # Dépendances Python
├── .env                     # Fichier de configuration
└── README.md                # Ce fichier
```

---

## ⚠️ Prérequis

- ✅ Python 3.9 ou supérieur
- 🔐 Compte sur [Groq](https://console.groq.com/keys) pour obtenir une clé API
- 📂 Git (optionnel, pour le versionnage)

---

## ⚙️ Installation & Configuration

### 1. Cloner le dépôt

```bash
git clone https://github.com/votre-pseudo/cv-analyzer.git
cd cv-analyzer
```

### 2. Créer et activer l’environnement virtuel

```bash
python -m venv venv
source venv/bin/activate     # Linux/macOS
venv\Scripts\activate        # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Obtenir une clé API Groq

Rendez-vous ici : [https://console.groq.com/keys](https://console.groq.com/keys)

### 5. Créer le fichier `.env`

Créez un fichier `.env` à la racine :

```bash
touch .env
```

Et ajoutez-y votre clé :

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ❗ Ne publiez jamais votre clé dans un repo public !

---

## ▶️ Lancement

```bash
uvicorn main:app --reload
```

Accédez à l’application :
🔗 [http://localhost:8000](http://localhost:8000)

Documentation interactive :
🔗 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔌 Utilisation de l'API

### Endpoint disponible

```
POST /analyze_cv
```

## 💡 À venir

- ✅ Support des fichiers PDF (via `PyPDF2` ou `pdfplumber`)
- 🧠 Prompt personnalisable selon les métiers cibles

---
```
