# Projet Fédérateur BDIA — Système intelligent de détection des plantes et des maladies foliaires

## Objectif

Ce projet a pour but de développer une application capable d'identifier automatiquement l'espèce d'une plante à partir d'une photo de feuille, puis de diagnostiquer les éventuelles maladies associées, afin d'aider à la détection précoce et à la réduction des pertes agricoles.

Plus précisément, l'application permet de :
- Identifier l'espèce de la plante à partir d'une image (classification par CNN)
- Détecter et classifier les maladies spécifiques à chaque plante (pomme, maïs, raisin, tomate, pomme de terre)
- Fournir des recommandations de traitement adaptées
- Alerter l'utilisateur en fonction des conditions météo pouvant favoriser certaines maladies
- Dialoguer avec un chatbot pour obtenir des conseils

## Dataset

L'application s'appuie sur le dataset **PlantVillage**, une base de données publique de référence en vision par ordinateur appliquée à l'agriculture, contenant des images annotées de feuilles saines et malades pour plusieurs espèces de plantes.

## Architecture

Le projet est composé de deux parties :

- **`frontend/`** — Application mobile développée avec **React Native** (Expo Router), permettant à l'utilisateur de s'inscrire/se connecter, prendre ou importer une photo de feuille, consulter le diagnostic, recevoir des alertes météo et discuter avec le chatbot.
- **`backend/`** — API développée avec **FastAPI** (Python), qui expose les routes d'authentification, de prédiction (modèles CNN entraînés avec TensorFlow/Keras), d'alertes météo (OpenWeather) et de chatbot, avec une base de données **MongoDB**.
- **`models/`** — Modèles de classification entraînés (un modèle par type de plante : pomme, maïs, raisin, tomate, pomme de terre, ainsi qu'un modèle de reconnaissance du type de plante).
- **`Livrables/`** — Documents de spécification et d'exploration des données du projet (cahier des charges, notebook d'exploration, schéma d'architecture).

## Stack technique

| Côté | Technologies |
|---|---|
| Frontend | React Native, Expo, Expo Router, TypeScript |
| Backend | FastAPI, Python, TensorFlow/Keras, PyMongo/Motor |
| Base de données | MongoDB |
| Authentification | JWT (python-jose), hachage bcrypt (passlib) |
| Données météo | API OpenWeather |

## Lancer le projet en local

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm start
```

## Structure du dépôt

```
Projet-federateur-BDIA-1-main/
├── backend/        # API FastAPI
├── frontend/       # Application mobile Expo/React Native
├── models/         # Modèles de classification (CNN)
├── Livrables/       # Documentation du projet
└── README.md
```

## Contexte

Projet réalisé dans le cadre du cursus BDIA (Big Data & Intelligence Artificielle) — Projet Fédérateur.
