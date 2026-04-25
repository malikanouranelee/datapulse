# DataPulse - Analyse des tendances musicales Spotify

Projet Data Science end-to-end : nettoyage - exploration - visualisation - machine learning

## Description

DataPulse analyse les tendances musicales a partir de donnees Spotify.
Pipeline complet : nettoyage, exploration, visualisation et machine learning.

## Dataset

- Source : Spotify Tracks Dataset Kaggle
- Volume : 114 000 morceaux -> 89 740 apres nettoyage
- Genres : 113 genres - 31 437 artistes uniques

## Installation

git clone https://github.com/malikanouranelee/datapulse.git
cd datapulse
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

## Utilisation

jupyter notebook notebooks/01_EDA.ipynb
streamlit run app/dashboard.py
jupyter notebook 02_ML.ipynb

## Resultats

- Genre le plus populaire : K-pop 59.4/100
- Correlation Energy / Loudness : +0.76
- Correlation Energy / Acousticness : -0.73
- Accuracy Random Forest : 46.43%

## Stack

Python - pandas - matplotlib - seaborn - plotly - streamlit - scikit-learn

## Auteure

Malika Mouliom - Projet Data Science 3e annee - Avril 2026
