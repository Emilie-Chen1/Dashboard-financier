# 💹 Dashboard Financier

Dashboard interactif pour analyser vos ratios financiers en quelques clics.

---
🎯 Objectif

Ce dashboard a été conçu pour simplifier l'analyse financière des entreprises en automatisant le calcul et la visualisation des principaux ratios financiers.

---
Pourquoi ?
---

✅ Gain de temps : Calculs automatiques des 7 ratios clés

✅ Visualisation claire : Graphiques interactifs et synthèse intelligente

✅ Alertes automatiques : Identification des zones de risque

---

## 🚀 Installation rapide (2 minutes)

```bash
# 1. Installer les dépendances
pip install streamlit pandas plotly openpyxl matplotlib

# 2. Lancer l'application
streamlit run app.py
```

L'application s'ouvre automatiquement dans votre navigateur à `http://localhost:8501`

---

## 📊 Utilisation

### 1️⃣ Télécharger le template

Cliquez sur **"📥 Télécharger le template Excel"** dans l'interface pour obtenir un fichier exemple pré-formaté.

### 2️⃣ Remplir vos données

Ouvrez le fichier Excel et remplacez les données d'exemple par vos propres chiffres :

| Colonne obligatoire | Exemple |
|---------------------|---------|
| Année | 2020, 2021, 2022... |
| Chiffre d'affaires | 1 000 000 |
| Résultat net | 100 000 |
| Actif total | 2 000 000 |
| Capitaux propres | 800 000 |
| Actif courant | 600 000 |
| Passif courant | 400 000 |
| Dettes totales | 1 200 000 |
| Trésorerie | 150 000 |
| Créances clients | 200 000 |

**💡 Conseils :**
- Minimum 2 années de données
- Recommandé : 5 années
- Pas de formules Excel (remplacer par valeurs)
- Pas de cellules vides

### 3️⃣ Importer et analyser

Glissez-déposez votre fichier Excel dans l'interface. L'analyse se fait automatiquement !

---

## 📈 Ce que vous obtenez

### 4 KPI principaux
- 💰 **Chiffre d'affaires** (avec évolution moyenne/an)
- 📈 **Résultat net** (avec évolution moyenne/an)
- 🎯 **ROE** - Rentabilité des capitaux propres
- ⚖️ **Endettement** - Poids de la dette

### 7 ratios financiers calculés
1. **Marge nette** - Rentabilité sur CA
2. **ROA** - Rentabilité sur actifs
3. **ROE** - Rentabilité pour actionnaires
4. **Liquidité générale** - Capacité à payer les dettes CT
5. **Liquidité immédiate** - Liquidité disponible immédiatement
6. **Endettement** - Dettes / Capitaux propres
7. **Autonomie financière** - Indépendance financière

### Graphiques interactifs
- Évolution des ratios année par année
- Comparaison N vs N-1 en %
- Sélection multiple de ratios

### Synthèse intelligente
Classification automatique :
- ✅ **Ratios optimaux** - Au-dessus du seuil optimal
- ⚠️ **Ratios acceptables** - Entre minimum et optimal
- 🚨 **Ratios en risque** - En dessous du seuil minimum

---

## 🎯 Seuils de référence

| Ratio | Optimal | Acceptable | Risque |
|-------|---------|------------|--------|
| Marge nette | ≥ 10% | 5-10% | < 5% |
| ROA | ≥ 10% | 5-10% | < 5% |
| ROE | ≥ 15% | 10-15% | < 10% |
| Liquidité générale | ≥ 1.5 | 1.0-1.5 | < 1.0 |
| Liquidité immédiate | ≥ 1.0 | 0.5-1.0 | < 0.5 |
| Endettement | ≤ 1.0 | 1.0-2.0 | > 2.0 |
| Autonomie financière | ≥ 50% | 30-50% | < 30% |

---

## 🎨 Personnalisation

Pour adapter les seuils à votre secteur, modifiez le fichier **`config.py`** :

```python
SEUILS_SECURITE = {
    "Marge nette": {
        "min": 0.05,      # 5% - Modifiez selon vos besoins
        "optimal": 0.10,  # 10%
        "label": "5%",
        "optimal_label": "10%"
    },
    # ... autres ratios
}
```

---

## ❓ FAQ

**Q : Quel format de fichier ?**  
R : Uniquement Excel (.xlsx). Pas de .xls ni .csv.

**Q : Mes données sont-elles sécurisées ?**  
R : Oui, tout fonctionne en local. Rien n'est envoyé sur internet.

**Q : Combien d'années minimum ?**  
R : 2 années minimum.

**Q : Erreur "colonnes manquantes" ?**  
R : Vérifiez que votre fichier contient les 10 colonnes requises avec les noms exacts.

**Q : Les formules Excel fonctionnent-elles ?**  
R : Non. Remplacez-les par leurs valeurs (Copier → Coller valeurs).

---

## 🐛 Problèmes courants

### L'application ne se lance pas
```bash
# Vérifier Python (doit être 3.8+)
python --version

# Réinstaller les dépendances
pip install --upgrade pip
pip install streamlit pandas plotly openpyxl matplotlib
```

### Erreur "colonnes manquantes"
- Téléchargez le template pour avoir les bons noms de colonnes
- Vérifiez les accents (ex: "d'affaires" et non "d'affaires")

### Les graphiques ne s'affichent pas
- Sélectionnez au moins un ratio dans la liste
- Actualisez la page (F5)

---

## 📂 Structure du projet

```
finance_dashboard/
├── app.py              # Application principale
├── config.py           # Configuration et seuils
├── styles.py           # Styles CSS
├── requirements.txt    # Dépendances
└── utils/
    ├── ratios.py       # Calcul des ratios
    └── synthese.py     # Analyse et synthèse
```

---

## 🛠️ Technologies

- **Streamlit** - Interface web
- **Pandas** - Manipulation des données
- **Plotly** - Graphiques interactifs
- **OpenPyXL** - Lecture Excel

---

## 👥 Auteurs

**CHEN Emilie** & **TOUSSAH Harrol**  

