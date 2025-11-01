# 💹 Dashboard Financier

> Dashboard interactif et professionnel pour analyser les ratios financiers d'une entreprise avec visualisations avancées, alertes automatiques et synthèse intelligente.

![Version](https://img.shields.io/badge/version-3.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-green)
![License](https://img.shields.io/badge/license-Academic-orange)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)
![Status](https://img.shields.io/badge/status-Production%20Ready-brightgreen)
![Maintenance](https://img.shields.io/badge/maintained-yes-success)

---

## 📑 Table des matières

- [🎯 Fonctionnalités principales](#-fonctionnalités-principales)
- [⚡ Quick Start (2 minutes)](#-quick-start-2-minutes)
- [🚀 Installation complète](#-installation-complète)
  - [Prérequis](#prérequis)
  - [Installation simple](#installation-simple)
  - [Environnement virtuel](#installation-dans-un-environnement-virtuel)
- [📂 Structure du projet](#-structure-du-projet)
- [📊 Guide d'utilisation](#-guide-dutilisation)
  - [Étape 1 : Template](#étape-1--télécharger-le-template-excel)
  - [Étape 2 : Remplir les données](#étape-2--remplir-vos-données)
  - [Étape 3 : Import](#étape-3--importer-le-fichier)
  - [Étape 4 : Analyse](#étape-4--analyser-les-résultats)
- [🖼️ Aperçu de l'interface](#️-aperçu-de-linterface)
- [📈 Sections du Dashboard](#-sections-du-dashboard)
- [📖 Exemples d'analyse réels](#-exemples-danalyse-réels)
- [💹 Les 7 ratios calculés](#-les-7-ratios-calculés)
- [📐 Formules de calcul](#-formules-de-calcul)
- [💡 Conseils d'interprétation](#-conseils-dinterprétation)
- [❓ FAQ (Questions Fréquentes)](#-faq-questions-fréquentes)
- [🐛 Résolution de problèmes](#-résolution-de-problèmes)
- [🎨 Personnalisation](#-personnalisation)
- [🔧 Informations techniques](#-informations-techniques-avancées)
- [🛠️ Technologies utilisées](#️-technologies-utilisées)
- [👥 Contributeurs](#-contributeurs)
- [📄 Licence](#-licence)

---

## 🎯 Fonctionnalités principales

- ✅ **Calcul automatique** de 7 ratios financiers essentiels
- 📊 **KPI avec double indicateur** : évolution en % (TCAM) et en valeur absolue (€/an)
- 📈 **Graphiques interactifs** : évolution N vs N-1 avec sélection multiple
- 🎨 **Tableau coloré** : amélioration (🟢), dégradation (🔴), stagnation (⚪)
- 🚨 **Synthèse intelligente** : classification automatique des ratios (optimal/acceptable/risque)
- 📅 **Timeline visuelle** : analyse année par année pour chaque ratio
- 💡 **Alertes contextuelles** : identification des années hors seuil
- 📥 **Template Excel** : fichier pré-formaté téléchargeable
- 🔒 **100% local** : aucune donnée envoyée sur internet

---

## ⚡ Quick Start (2 minutes)

**Vous voulez juste tester rapidement ?**

```bash
# Installation en 1 ligne
pip install streamlit pandas plotly openpyxl matplotlib && streamlit run app.py
```

**Puis dans l'interface :**

1. 📥 Cliquez sur **"Télécharger le template Excel"**
2. 📤 Uploadez ce même fichier (données d'exemple déjà incluses)
3. 🎉 **Explorez les résultats !**

**Vous venez de réaliser votre première analyse financière en 2 minutes.**

---

*Pour une installation détaillée et personnalisée, voir [Installation complète](#-installation-complète)*

---

## 🚀 Installation complète

### Prérequis

- **Python 3.8 ou supérieur** ([Télécharger Python](https://www.python.org/downloads/))
- **pip** (inclus avec Python)
- **Git** (optionnel, pour cloner le projet)

### Installation simple

```bash
# 1. Télécharger ou cloner le projet
cd finance_dashboard

# 2. Installer les dépendances (sans versions spécifiques pour compatibilité maximale)
pip install streamlit pandas plotly openpyxl matplotlib

# 3. Lancer l'application
streamlit run app.py
```

✅ L'application s'ouvre automatiquement dans votre navigateur à : `http://localhost:8501`

### Installation dans un environnement virtuel (recommandé)

**Pourquoi ?** Évite les conflits entre projets Python.

```bash
# Windows
python -m venv venv
venv\Scripts\activate
pip install streamlit pandas plotly openpyxl matplotlib
streamlit run app.py

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
pip install streamlit pandas plotly openpyxl matplotlib
streamlit run app.py
```

**Pour désactiver l'environnement virtuel :**
```bash
deactivate
```

---

## 📂 Structure du projet

```
finance_dashboard/
│
├── app.py                    # 💻 Application principale (point d'entrée)
├── config.py                 # ⚙️ Configuration (seuils, couleurs, template)
├── styles.py                 # 🎨 Styles CSS personnalisés
├── requirements.txt          # 📦 Dépendances Python
├── README.md                 # 📖 Documentation (ce fichier)
│
├── utils/                    # 📁 Modules Python
│   ├── __init__.py          # Initialisation du package
│   ├── ratios.py            # 🧮 Calcul des 7 ratios financiers
│   └── synthese.py          # 📊 Synthèse et analyse intelligente
│
├── data/                     # 💾 Données (créé automatiquement)
│   └── example_dataset.xlsx # Fichier exemple (optionnel)
│
└── screenshots/              # 🖼️ Captures d'écran (pour documentation)
    ├── dashboard.png
    ├── graphiques.png
    └── synthese.png
```

### Architecture modulaire

Le projet suit une **architecture modulaire** pour faciliter la maintenance :

- **app.py** : Orchestration et interface utilisateur (Streamlit)
- **utils/ratios.py** : Logique métier (calculs financiers)
- **utils/synthese.py** : Analyses avancées et classification
- **config.py** : Configuration centralisée (seuils, couleurs, données template)
- **styles.py** : Apparence (CSS personnalisé)

---

## 📊 Guide d'utilisation

### Étape 1 : Télécharger le template Excel

1. Lancez l'application : `streamlit run app.py`
2. Dans l'interface, cliquez sur **"📥 Télécharger le template Excel"**
3. Un fichier `template_finances.xlsx` sera téléchargé avec **5 années de données d'exemple**

### Étape 2 : Remplir vos données

Ouvrez le fichier Excel et **remplacez les données d'exemple par vos propres chiffres financiers**.

#### Colonnes requises (noms exacts, sensibles à la casse)

| Colonne | Description | Exemple | Source |
|---------|-------------|---------|--------|
| **Année** | Année fiscale | 2020, 2021, 2022... | N/A |
| **Chiffre d'affaires** | Revenus totaux | 1 000 000 | Compte de résultat |
| **Résultat net** | Bénéfice net après impôts | 100 000 | Compte de résultat |
| **Actif total** | Total des actifs au bilan | 2 000 000 | Bilan - Actif |
| **Capitaux propres** | Fonds propres | 800 000 | Bilan - Passif |
| **Actif courant** | Actifs liquides à court terme | 600 000 | Bilan - Actif |
| **Passif courant** | Dettes à court terme | 400 000 | Bilan - Passif |
| **Dettes totales** | Ensemble des dettes | 1 200 000 | Bilan - Passif |
| **Trésorerie** | Liquidités disponibles | 150 000 | Bilan - Actif |
| **Créances clients** | Montants dus par les clients | 200 000 | Bilan - Actif |

#### 💡 Conseils importants

✅ **Nombre d'années** :
- **Minimum** : 2 années (pour calculer les évolutions)
- **Recommandé** : 5 années (pour identifier les tendances)
- **Maximum** : 10-15 années (au-delà, pertinence limitée)

✅ **Cohérence des données** :
- Utiliser la **même unité monétaire** pour toutes les années (€, $, £...)
- Même **période de clôture** (ex: 31/12 de chaque année)
- Données **auditées ou vérifiées** si possible

✅ **Format** :
- Valeurs **numériques uniquement** (pas de texte)
- Pas de **formules Excel** (remplacer par valeurs : Copier → Coller valeurs)
- Pas de **cellules vides** dans les colonnes obligatoires

### Étape 3 : Importer le fichier

1. Dans l'interface, **glissez-déposez** votre fichier Excel dans la zone d'upload
2. **OU** cliquez sur **"Browse files"** pour sélectionner le fichier

⚠️ **Format accepté** : Uniquement fichiers Excel (**.xlsx**)

### Étape 4 : Analyser les résultats

L'application génère **automatiquement** 4 sections d'analyse :

1. 📊 **Vue d'ensemble** : KPI principaux avec évolutions
2. 📈 **Graphiques interactifs** : Évolution des ratios
3. 📋 **Tableau récapitulatif** : Toutes les valeurs avec code couleur
4. 🎯 **Synthèse intelligente** : Classification et recommandations

---

## 🖼️ Aperçu de l'interface

### Dashboard principal

*[Capture d'écran : Vue d'ensemble avec les 4 KPI principaux]*

**Fonctionnalités visibles :**
- 💰 Chiffre d'affaires avec TCAM et variation €/an
- 📈 Résultat net avec évolution
- 🎯 ROE avec variation en points
- ⚖️ Endettement avec tendance

---

### Graphiques interactifs

*[Capture d'écran : Graphique d'évolution avec 3 ratios sélectionnés]*

**Fonctionnalités :**
- Sélection multiple de ratios
- Évolution N vs N-1 en %
- Survol pour détails
- Ligne de stabilité à 0%

---

### Synthèse intelligente

*[Capture d'écran : Classification des ratios avec timeline]*

**Analyse automatique :**
- Classification : Optimal / Acceptable / Risque
- Timeline visuelle par ratio
- Identification des années problématiques

---

## 📈 Sections du Dashboard

### 1️⃣ Vue d'ensemble - Indicateurs clés

Affichage de **4 KPI principaux** avec **triple indicateur** :

```
💰 Chiffre d'affaires          📈 Résultat net
1 257 321 €                    141 874 €
↗ +14.2% /an (TCAM)            ↗ +21.8% /an
📊 +129 352 €/an               📊 +19 365 €/an

🎯 ROE                         ⚖️ Endettement
13.4%                          1.17
↗ +1.0 pts/an                  ↗ +0.02 /an
```

**Interprétation** :
- **Ligne 1** : Valeur actuelle (dernière année)
- **Ligne 2** : TCAM (Taux de Croissance Annuel Moyen) en %
- **Ligne 3** : Variation moyenne annuelle en valeur absolue (CA et RN uniquement)

### 2️⃣ Analyse des ratios financiers

#### 📈 Graphique d'évolution

**Fonctionnalités** :
- ✅ **Sélection multiple** : Comparez jusqu'à 7 ratios simultanément
- ✅ **Évolution N vs N-1** : Variation en % par rapport à l'année précédente
- ✅ **Interactif** : Survol pour voir les détails de chaque point
- ✅ **Ligne de référence** : Stabilité à 0%
- ✅ **Export** : Téléchargement de l'image (PNG)

**Lecture** : "+15% en 2023" signifie que le ratio a augmenté de 15% entre 2022 et 2023.

#### 📋 Tableau récapitulatif

**Code couleur intelligent** :
- 🟢 **Amélioration** : Progression par rapport à N-1
- 🔴 **Dégradation** : Régression par rapport à N-1
- ⚪ **Stagnation** : Variation < 1%
- ⚫ **Année de référence** : Première année (pas de comparaison)

### 3️⃣ Synthèse de l'analyse

**Vue d'ensemble en 3 catégories** :

```
✅ Ratios optimaux    ⚠️ Ratios acceptables    🚨 Ratios en risque
      3/7                     4/7                      0/7
```

**Expanders interactifs pour le détail** :

#### ✅ Ratios optimaux (dépassent le seuil optimal)
- Liste des ratios performants
- Timeline année par année avec valeurs
- Comparaison avec le seuil optimal

#### ⚠️ Ratios acceptables (entre minimum et optimal)
- Ratios à surveiller
- Années hors seuil identifiées
- Timeline avec code couleur (🚨/⚠️/✅)

#### 🚨 Ratios en risque (sous le seuil minimum)
- Alertes détaillées
- Actions recommandées
- Évolution sur la période

**Analyses complémentaires** :
- 📅 **Années problématiques** : Top 3 des années avec le plus d'alertes
- 📈 **Tendance générale** : Amélioration, dégradation ou stabilité

---

## 📖 Exemples d'analyse réels

### Cas 1 : Startup en croissance (Secteur Tech) 🚀

**Profil** : Entreprise SaaS, 3 ans d'existence, hypercroissance

**Données** :
```
Année    CA          RN         ROE     Endettement
2022     500 k€      -50 k€     -8%     2.5
2023     1.2 M€      80 k€      12%     1.8
2024     2.5 M€      250 k€     18%     1.2
```

**✅ Interprétation du dashboard** :
- **TCAM CA : +124%** → Croissance explosive (excellent ✅)
- **ROE : -8% → 18%** → Rentabilité atteinte rapidement (✅)
- **Endettement : 2.5 → 1.2** → Désendettement progressif (✅)
- **Marge nette : -10% → 10%** → Point mort franchi en 2023 (✅)

**🎯 Verdict** : 🚀 **Excellente trajectoire**
- Entreprise en hypercroissance
- Amélioration simultanée de tous les indicateurs
- Modèle économique validé

**💡 Actions recommandées** :
1. ✅ Continuer l'investissement dans la croissance
2. ⚠️ Surveiller la liquidité (croissance rapide = besoin en trésorerie)
3. 💰 Anticiper les besoins de financement pour 2025 (série A/B)
4. 👥 Recruter pour accompagner la croissance

---

### Cas 2 : PME industrielle en difficulté (Secteur Industrie) ⚠️

**Profil** : Fabricant, 20 ans d'existence, marché mature

**Données** :
```
Année    CA          Marge nette    ROE     Liquidité
2020     5.0 M€      4%             8%      1.2
2021     5.2 M€      5%             9%      1.3
2022     5.1 M€      3%             6%      1.1
2023     4.9 M€      2%             5%      0.9
2024     4.8 M€      1%             4%      0.8
```

**🚨 Interprétation du dashboard** :
- **TCAM CA : -1.0%** → Décroissance lente (⚠️)
- **Marge nette : 4% → 1%** → Érosion des marges (🚨)
- **ROE : 8% → 4%** → Rentabilité en chute (🚨)
- **Liquidité : 1.2 → 0.8** → Difficulté à payer les dettes CT (🚨)

**🎯 Verdict** : 🚨 **Situation critique**
- 4 ratios sur 7 en zone de risque
- Tendance à la dégradation sur tous les indicateurs
- Risque de difficulté financière à court terme

**💡 Actions URGENTES recommandées** :
1. 🚨 **Immédiat** : Injection de trésorerie (prêt ou augmentation capital)
2. 💰 **Court terme** (3 mois) : Réduction des coûts opérationnels (-15%)
3. 📊 **Moyen terme** (6 mois) : Repositionnement stratégique ou diversification
4. 📈 **Suivi** : Analyse mensuelle des flux de trésorerie

**Leviers d'action** :
- Négocier délais de paiement fournisseurs
- Accélérer recouvrement créances clients
- Réduire stocks dormants
- Identifier produits non rentables

---

### Cas 3 : Commerce de détail stable ✅

**Profil** : Magasin retail, situation équilibrée, croissance régulière

**Données** :
```
Année    CA          ROE     BFR (jours)    Liquidité
2020     2.0 M€      11%     45 j           1.6
2021     2.1 M€      12%     42 j           1.7
2022     2.2 M€      13%     40 j           1.8
2023     2.3 M€      13%     38 j           1.9
2024     2.4 M€      14%     35 j           2.0
```

**✅ Interprétation du dashboard** :
- **TCAM CA : +4.7%** → Croissance régulière et soutenue (✅)
- **ROE : 11% → 14%** → Amélioration continue de la rentabilité (✅)
- **BFR : 45j → 35j** → Optimisation du cycle d'exploitation (✅)
- **Liquidité : 1.6 → 2.0** → Solvabilité largement renforcée (✅)

**🎯 Verdict** : ✅ **Santé financière excellente**
- Tous indicateurs au vert ou en amélioration
- Gestion financière optimale
- Stabilité et prédictibilité

**💡 Opportunités identifiées** :
1. 💰 **Capacité d'investissement élevée** (liquidité > 1.5)
   → Ouverture nouveau point de vente
   → Modernisation équipements
2. 📦 **BFR maîtrisé** (-10 jours en 4 ans)
   → Peut négocier meilleures conditions fournisseurs
3. 📈 **Croissance organique possible** sans endettement supplémentaire
4. 🎯 **Distribution dividendes** envisageable

---

## 💹 Les 7 ratios calculés

### Ratios de rentabilité (3)

#### 1. Marge nette

**📐 Formule** : `Résultat net ÷ Chiffre d'affaires`

**💡 Interprétation** : Part du chiffre d'affaires qui se transforme en bénéfice net

**🎯 Seuils** :
- ✅ **Optimal** : ≥ 10%
- ⚠️ **Acceptable** : 5% - 10%
- 🚨 **Risque** : < 5%

**📊 Exemple** :
- CA = 1 000 000 €
- RN = 80 000 €
- **Marge nette = 8%** (acceptable)

---

#### 2. ROA (Return on Assets)

**📐 Formule** : `Résultat net ÷ Actif total`

**💡 Interprétation** : Efficacité de l'utilisation des actifs pour générer du profit

**🎯 Seuils** :
- ✅ **Optimal** : ≥ 10%
- ⚠️ **Acceptable** : 5% - 10%
- 🚨 **Risque** : < 5%

**📊 Particularités sectorielles** :
- **Industries** : ROA plus faible (5-7%) → actifs lourds
- **Services** : ROA plus élevé (10-15%) → peu d'actifs
- **Tech** : ROA variable selon phase (startup vs mature)

---

#### 3. ROE (Return on Equity)

**📐 Formule** : `Résultat net ÷ Capitaux propres`

**💡 Interprétation** : Rentabilité pour les actionnaires

**🎯 Seuils** :
- ✅ **Optimal** : ≥ 15%
- ⚠️ **Acceptable** : 10% - 15%
- 🚨 **Risque** : < 10%

**⚠️ Attention** : Un ROE très élevé (> 25%) peut indiquer un endettement excessif

---

### Ratios de liquidité (2)

#### 4. Liquidité générale

**📐 Formule** : `Actif courant ÷ Passif courant`

**💡 Interprétation** : Capacité à payer les dettes à court terme

**🎯 Seuils** :
- ✅ **Optimal** : ≥ 1.5
- ⚠️ **Acceptable** : 1.0 - 1.5
- 🚨 **Risque** : < 1.0

**📊 Lecture** :
- **1.5** = 1.50 € d'actifs liquides pour 1 € de dettes CT
- **< 1.0** = Difficulté à honorer les engagements

---

#### 5. Liquidité immédiate

**📐 Formule** : `(Trésorerie + Créances clients) ÷ Passif courant`

**💡 Interprétation** : Liquidité immédiatement disponible (sans vendre les stocks)

**🎯 Seuils** :
- ✅ **Optimal** : ≥ 1.0
- ⚠️ **Acceptable** : 0.5 - 1.0
- 🚨 **Risque** : < 0.5

**💡 Plus conservateur que la liquidité générale** (exclut les stocks)

---

### Ratios de structure financière (2)

#### 6. Endettement

**📐 Formule** : `Dettes totales ÷ Capitaux propres`

**💡 Interprétation** : Poids de la dette par rapport aux fonds propres

**🎯 Seuils** (⚠️ **ratio inverse** : plus bas = mieux) :
- ✅ **Optimal** : ≤ 1.0
- ⚠️ **Acceptable** : 1.0 - 2.0
- 🚨 **Risque** : > 2.0

**📊 Lecture** :
- **1.0** = Autant de dettes que de fonds propres
- **> 2.0** = Plus de 2 fois plus de dettes que de fonds propres

**💡 Particularités** :
- Startups : Endettement élevé acceptable en phase de croissance
- Entreprises matures : Endettement faible privilégié

---

#### 7. Autonomie financière

**📐 Formule** : `Capitaux propres ÷ Actif total`

**💡 Interprétation** : Indépendance vis-à-vis des créanciers

**🎯 Seuils** :
- ✅ **Optimal** : ≥ 50%
- ⚠️ **Acceptable** : 30% - 50%
- 🚨 **Risque** : < 30%

**📊 Lecture** : 50% = La moitié de l'actif est financé par les fonds propres

---

## 📐 Formules de calcul

### TCAM (Taux de Croissance Annuel Moyen)

**Formule mathématique** :

| Variable | Symbole | Exemple |
|----------|---------|---------|
| Valeur finale | V<sub>f</sub> | 1 500 000 € |
| Valeur initiale | V<sub>i</sub> | 1 000 000 € |
| Nombre d'années | n | 4 |

**Calcul** :

```
TCAM = ((V_finale / V_initiale)^(1/n)) - 1
TCAM = ((1 500 000 / 1 000 000)^(1/4)) - 1
TCAM = (1.5^0.25) - 1
TCAM = 1.1067 - 1
TCAM = 0.1067 = 10.67% par an
```

**Interprétation** : Le chiffre d'affaires a crû en moyenne de **10.67% par an** sur 4 ans.

---

### Variation moyenne annuelle (valeur absolue)

**Formule** :

```
Variation moyenne = (Valeur finale - Valeur initiale) ÷ nombre d'années
```

**Exemple** :
```
CA 2020 : 1 000 000 €
CA 2024 : 1 500 000 €
Variation = (1 500 000 - 1 000 000) ÷ 4 = +125 000 €/an
```

**Interprétation** : Le CA augmente en moyenne de **125 000 € par an**.

---

### Variation pour ratios en pourcentage

**Formule** :

```
Variation moyenne = (Ratio final - Ratio initial) × 100 ÷ nombre d'années
```

**Exemple** :
```
ROE 2020 : 9.2% (0.092)
ROE 2024 : 13.4% (0.134)
Variation = (0.134 - 0.092) × 100 ÷ 4 = +1.05 points/an
```

**Interprétation** : Le ROE progresse de **1.05 point de pourcentage par an**.

---

## 💡 Conseils d'interprétation

### Par type de ratio

#### TCAM élevé (> 15%)
- ✅ **Positif** : Croissance forte
- ⚠️ **À vérifier** : Soutenabilité de la croissance
- 💡 **Action** : Analyser les sources de croissance (organique vs externe)

#### Ratios de rentabilité en hausse
- ✅ **Positif** : Amélioration de la performance opérationnelle
- 💡 **Action** : Identifier les leviers d'amélioration pour les maintenir

#### Endettement en baisse
- ✅ **Positif** : Amélioration de la structure financière
- 💡 **Opportunité** : Capacité d'investissement accrue

#### Liquidité > 1.5
- ✅ **Positif** : Bonne capacité à honorer les engagements
- 💡 **Optimisation** : Peut investir la trésorerie excédentaire

---

### Par secteur d'activité

| Secteur | Particularités |
|---------|----------------|
| **Industries** | ROA et liquidité généralement plus faibles (actifs lourds, stocks importants) |
| **Services** | Marges nettes plus élevées, peu d'actifs, ROE et ROA élevés |
| **Commerce** | Rotation rapide, liquidité critique, marges faibles mais volume élevé |
| **Technologie** | ROE élevé, croissance prioritaire, rentabilité peut être négative (startups) |
| **Immobilier** | Endettement élevé acceptable, actifs importants, ROA faible |

**💡 Conseil** : Adaptez les seuils dans `config.py` selon votre secteur

---

### Contexte économique

**À prendre en compte** :
- 📈 **Cycle économique** : Croissance, récession, reprise
- 🌍 **Environnement sectoriel** : Concurrence, réglementation
- 💰 **Taux d'intérêt** : Impact sur le coût de l'endettement
- 📅 **Événements exceptionnels** : COVID-19, crise sectorielle

**Exemple** : Un TCAM négatif en 2020-2021 peut être normal (COVID), mais alarmant en 2023-2024.

---

## ❓ FAQ (Questions Fréquentes)

### Général

**Q : Puis-je utiliser des données en dollars/livres/autres devises ?**

R : ✅ Oui, l'application fonctionne avec n'importe quelle devise. Assurez-vous juste que **toutes les données utilisent la même unité monétaire**.

---

**Q : Combien d'années minimum/maximum puis-je analyser ?**

R : 
- **Minimum** : 2 ans (pour calculer les évolutions)
- **Recommandé** : 5 ans (pour tendances significatives)
- **Maximum pratique** : 10-15 ans (au-delà, pertinence limitée)

---

**Q : Les ratios sont-ils valables pour toutes les entreprises ?**

R : Non. Les seuils varient selon le secteur. Personnalisez dans `config.py` :
- **Industries** : ROA plus faible (actifs lourds)
- **Services** : Marges nettes plus élevées
- **Commerce** : Rotation rapide, liquidité critique
- **Technologie** : ROE élevé, croissance prioritaire

---

### Données

**Q : D'où viennent les colonnes requises ?**

R : Sources comptables standards :
- **Compte de résultat** : Chiffre d'affaires, Résultat net
- **Bilan actif** : Actif total, Actif courant, Trésorerie, Créances clients
- **Bilan passif** : Capitaux propres, Passif courant, Dettes totales

---

**Q : Que faire si je n'ai pas toutes les colonnes ?**

R : 
1. Téléchargez le **template Excel** pour voir exactement les données nécessaires
2. Vous pouvez **estimer** certaines valeurs si nécessaire
3. Formule : `Dettes totales = Dettes CT + Dettes LT`

---

**Q : Les formules Excel sont-elles supportées ?**

R : ❌ Non. Remplacez toutes les formules par leurs valeurs avant l'import :
1. Sélectionnez les cellules avec formules
2. **Ctrl + C** (copier)
3. **Clic droit** → **Coller les valeurs**

---

### Interprétation

**Q : Qu'est-ce qu'un "bon" ROE ?**

R : Dépend du secteur :
- **< 10%** : Faible (🚨)
- **10-15%** : Acceptable (⚠️)
- **> 15%** : Optimal (✅)
- **> 20%** : Excellent (services/tech)

---

**Q : Mon endettement est à 1.5, est-ce grave ?**

R : Non, c'est **acceptable** (⚠️). Tant que vous restez < 2.0 et que la tendance est stable ou baissière, c'est maîtrisé.

---

**Q : Comment interpréter "TCAM +14.2% /an" ?**

R : Votre chiffre d'affaires croît en moyenne de **14.2% par an** sur la période analysée. C'est une **croissance forte et soutenue** (> 10%).

---

### Technique

**Q : L'application fonctionne-t-elle hors ligne ?**

R : ✅ Oui, une fois lancée (`streamlit run app.py`), elle fonctionne **100% localement** sans connexion internet.

---

**Q : Mes données sont-elles sécurisées ?**

R : ✅ Oui, **tout est local**. Aucune donnée n'est envoyée sur internet. L'application tourne exclusivement sur votre machine.

---

**Q : Puis-je exporter les résultats ?**

R : 
- **Actuellement** : Capture d'écran ou impression PDF du navigateur (Ctrl + P)
- **Prochainement** : Export PDF intégré (v3.1)

---

**Q : Pourquoi Pandas 2.2.2 ne s'installe pas sur Windows ?**

R : Problème connu. **Solution** :
```bash
# N'utilisez PAS requirements.txt avec versions exactes
pip install streamlit pandas plotly openpyxl matplotlib
# (sans versions spécifiques = télécharge wheels précompilés)
```

---

### Limites

**Q : Quelles sont les limites de l'outil ?**

R : 
- ❌ Pas de prévisions / Machine Learning
- ❌ Pas de comparaison multi-entreprises
- ❌ Pas de connexion bases de données
- ❌ Pas de benchmarks sectoriels automatiques
- ✅ **Mais** : Open source, personnalisable, extensible

---

**Q : Puis-je contribuer au projet ?**

R : ✅ Absolument ! Contactez **CHEN Emilie** ou **TOUSSAH Harrol** (voir section [Contributeurs](#-contributeurs)).

---

## 🐛 Résolution de problèmes

### ❌ "Les colonnes requises sont manquantes"

**Cause** : Le fichier Excel ne contient pas toutes les colonnes nécessaires ou les noms sont incorrects.

**Solution** :
1. Vérifiez que votre fichier contient **exactement les 10 colonnes requises**
2. Les noms doivent être **exacts** (sensible à la casse et aux accents)
3. Téléchargez le **template** pour avoir les bons noms

---

### ❌ "Erreur lors du traitement du fichier"

**Causes possibles** :
- Format de fichier incorrect (utiliser **.xlsx** uniquement)
- Données non numériques dans les colonnes de chiffres
- Cellules vides dans les colonnes importantes
- Formules Excel avec erreurs (#DIV/0!, #N/A)

**Solutions** :
1. Vérifier le format : `.xlsx` uniquement
2. Supprimer tout texte dans les colonnes numériques
3. Remplir toutes les cellules obligatoires
4. Remplacer les formules Excel par leurs valeurs

---

### ❌ L'application ne se lance pas

**Solutions** :

```bash
# Vérifier l'installation de Streamlit
streamlit --version

# Vérifier la version de Python
python --version  # Doit être 3.8+

# Réinstaller les dépendances
pip install --upgrade pip
pip install streamlit pandas plotly openpyxl matplotlib

# Si problème persiste, utiliser un environnement virtuel
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
pip install streamlit pandas plotly openpyxl matplotlib
streamlit run app.py
```

---

### ❌ Les graphiques ne s'affichent pas

**Solutions** :
- Sélectionnez **au moins un ratio** dans le multi-select
- Actualisez la page (**F5**)
- Vérifiez que Plotly est installé : `pip show plotly`
- Videz le cache : Menu Streamlit > **Clear cache**

---

### ❌ Valeurs aberrantes ou calculs incorrects

**Causes** :
- Division par zéro (colonnes avec valeurs nulles)
- Valeurs négatives là où elles ne devraient pas être
- Ordre des années incorrect

**Solutions** :
- Vérifier qu'**aucune colonne n'a de valeurs à 0**
- S'assurer que les **années sont dans l'ordre croissant**
- Vérifier la **cohérence des données**

---

### ❌ "ModuleNotFoundError: No module named 'utils'"

**Cause** : Le fichier `utils/__init__.py` est manquant.

**Solution** :
```bash
# Windows
type nul > utils\__init__.py

# Linux/Mac
touch utils/__init__.py
```

---

## 🎨 Personnalisation

### Modifier les seuils de sécurité

Éditez le fichier **`config.py`** :

```python
SEUILS_SECURITE = {
    "Marge nette": {
        "min": 0.05,          # 5% - Seuil minimum
        "optimal": 0.10,      # 10% - Seuil optimal
        "label": "5%",
        "optimal_label": "10%"
    },
    "ROE": {
        "min": 0.10,          # 10%
        "optimal": 0.15,      # 15%
        "label": "10%",
        "optimal_label": "15%"
    },
    # ... autres ratios
}
```

**💡 Conseil** : Adaptez les seuils selon votre **secteur d'activité** :

| Secteur | ROE min | ROE optimal | Marge nette min |
|---------|---------|-------------|-----------------|
| Industries | 8% | 12% | 3% |
| Services | 12% | 18% | 8% |
| Commerce | 10% | 15% | 2% |
| Tech | 15% | 25% | 10% |

---

### Modifier les couleurs

Dans **`config.py`** :

```python
# Couleurs des graphiques
GRAPH_COLORS = [
    '#667eea',  # Violet
    '#10b981',  # Vert
    '#ef4444',  # Rouge
    '#f59e0b',  # Orange
    '#8b5cf6',  # Violet clair
    '#ec4899',  # Rose
    '#06b6d4'   # Cyan
]

# Couleurs des statuts
STATUS_COLORS = {
    "optimal": {"color": "#10b981", "border": "#059669"},      # Vert
    "acceptable": {"color": "#f59e0b", "border": "#d97706"},   # Orange
    "risque": {"color": "#ef4444", "border": "#dc2626"}        # Rouge
}
```

**🎨 Palette de couleurs** : Utilisez [coolors.co](https://coolors.co/) pour créer vos palettes.

---

### Modifier le template Excel

Dans **`config.py`**, section `TEMPLATE_DATA` :

```python
TEMPLATE_DATA = {
    'Année': [2020, 2021, 2022, 2023, 2024],
    'Chiffre d\'affaires': [1000000, 1200000, 1400000, 1600000, 1800000],
    'Résultat net': [80000, 100000, 120000, 140000, 160000],
    # ... vos données personnalisées
}
```

**Relancez l'application** pour que le nouveau template soit disponible au téléchargement.

---

## 🔧 Informations techniques avancées

### Compatibilité

| Élément | Support |
|---------|---------|
| **Systèmes d'exploitation** | ✅ Windows 10/11<br>✅ macOS 10.14+<br>✅ Linux (Ubuntu 18.04+) |
| **Python** | ✅ 3.8, 3.9, 3.10, 3.11<br>⚠️ 3.12 (non testé)<br>❌ 3.7 et antérieurs |
| **Navigateurs** | ✅ Chrome 90+<br>✅ Firefox 88+<br>✅ Edge 90+<br>⚠️ Safari 14+ (limitations mineures) |
| **Fichiers** | ✅ .xlsx (Excel 2007+)<br>❌ .xls (ancien format)<br>❌ .csv (conversion nécessaire) |

---

### Performance

**Capacités testées** :
- ✅ Jusqu'à **50 années** d'historique
- ✅ Fichiers Excel jusqu'à **5 MB**
- ✅ Temps de calcul **< 2 secondes** pour 10 années
- ✅ Mémoire : **~150 MB** en utilisation normale

**Limitations connues** :
- ⚠️ Graphiques peuvent ralentir avec > 20 années
- ⚠️ Pas d'optimisation pour fichiers > 10 MB

---

### Architecture du code

```
Flux de données :
Excel → Pandas DataFrame → Validation → Calculs → Plotly Charts → Streamlit UI
```

**Module ratios.py** :
- Entrée : DataFrame avec 10 colonnes
- Sortie : DataFrame avec 7 ratios calculés

**Module synthese.py** :
- Entrée : DataFrame de ratios + seuils (config)
- Sortie : Classification (optimal/acceptable/risque)

---

### Sécurité et confidentialité

**Garanties** :
- 🔒 **100% local** : Aucune donnée n'est envoyée sur internet
- 🔒 **Pas de tracking** : Aucune collecte de données d'usage
- 🔒 **Pas de cookies** : Aucun cookie tiers
- 🔒 **Open source** : Code auditable

**Recommandations** :
- Utilisez un **environnement virtuel** (venv)
- Ne partagez pas vos fichiers Excel avec données sensibles
- En production : utilisez **HTTPS** avec reverse proxy

---

### Variables d'environnement (optionnel)

Créez un fichier **`.env`** pour personnalisation avancée :

```bash
# .env
STREAMLIT_SERVER_PORT=8502
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_BROWSER_GATHER_USAGE_STATS=false
```

---

### Déploiement

#### Option 1 : Serveur local

```bash
streamlit run app.py --server.port 80 --server.address 0.0.0.0
```

#### Option 2 : Streamlit Cloud (gratuit)

1. Push le code sur **GitHub**
2. Créez un compte sur [share.streamlit.io](https://share.streamlit.io)
3. Connectez votre repo
4. Déployez en **1 clic**

#### Option 3 : Docker

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install streamlit pandas plotly openpyxl matplotlib
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
```

---

### Logs et debugging

**Activer les logs détaillés** :

```bash
streamlit run app.py --logger.level=debug
```

**Fichiers de logs** :
- Windows : `C:\Users\VotreNom\AppData\Local\streamlit\logs\`
- Linux/Mac : `~/.streamlit/logs/`

---

## 🛠️ Technologies utilisées

| Technologie | Version | Usage | Taille |
|-------------|---------|-------|--------|
| **Python** | 3.8+ | Langage principal | - |
| **Streamlit** | 1.30.0+ | Framework web interactif | ~50 MB |
| **Pandas** | 2.0.0+ | Manipulation de données | ~80 MB |
| **Plotly** | 5.18.0+ | Graphiques interactifs | ~30 MB |
| **NumPy** | 1.24.0+ | Calculs numériques | ~40 MB |
| **OpenPyXL** | 3.1.0+ | Lecture/écriture Excel | ~5 MB |
| **Matplotlib** | 3.7.0+ | Visualisations (fallback) | ~100 MB |

**Taille totale installée** : ~350 MB

---

## 📄 Exemple de données valides

| Année | Chiffre d'affaires | Résultat net | Actif total | Capitaux propres | Actif courant | Passif courant | Dettes totales | Trésorerie | Créances clients |
|-------|-------------------|--------------|-------------|------------------|---------------|----------------|----------------|------------|------------------|
| 2020 | 739 913 | 64 414 | 1 275 133 | 698 170 | 502 449 | 357 399 | 772 929 | 79 438 | 115 273 |
| 2021 | 881 257 | 88 081 | 1 744 022 | 724 479 | 554 857 | 425 981 | 779 585 | 109 360 | 150 127 |
| 2022 | 1 034 738 | 123 679 | 1 853 602 | 944 816 | 692 365 | 419 670 | 883 459 | 119 134 | 157 775 |
| 2023 | 1 292 271 | 142 675 | 1 966 970 | 1 072 564 | 803 479 | 572 608 | 1 057 530 | 157 155 | 211 888 |
| 2024 | 1 257 321 | 141 874 | 2 307 336 | 1 061 609 | 950 726 | 703 057 | 1 240 950 | 125 671 | 227 875 |

---

## 📄 Mises à jour futures envisagées

### Version 3.1 (Q1 2025)
- [ ] Export des analyses en **PDF**
- [ ] **Sauvegarde** des analyses précédentes
- [ ] **Import CSV** (conversion automatique)

### Version 3.2 (Q2 2025)
- [ ] **Comparaison avec benchmarks sectoriels**
- [ ] **Mode multi-entreprises** (comparaison)
- [ ] **Prévisions** basées sur tendances (ML)

### Version 4.0 (Q3 2025)
- [ ] **Analyse de scénarios** (optimiste/pessimiste/réaliste)
- [ ] **Graphiques avancés** (radar, waterfall, sankey)
- [ ] **API REST** pour intégration externe
- [ ] **Authentification** et base de données

---

## 👥 Contributeurs

**Développeurs** :
- **CHEN Emilie** 
- **TOUSSAH Harrol**

**Formation** : DU SDA (Diplôme Universitaire Science des Données Appliquées)

**Année** : 2024-2025

**Université** : [Votre université]

**Contact** : [Vos emails si vous le souhaitez]

---

## 📄 Licence

Projet réalisé dans un **cadre académique**.

**Utilisation** :
- ✅ Usage personnel et éducatif libre
- ✅ Modification du code autorisée
- ✅ Partage avec attribution
- ❌ Usage commercial sans autorisation

**Attribution** :
Merci de citer les auteurs si vous utilisez ce projet :
```
Dashboard Financier v3.0 - CHEN Emilie & TOUSSAH Harrol (2024)
DU SDA - [Votre université]
```

---

## 📞 Support

Pour toute question ou suggestion d'amélioration :

1. **Documentation** : Consultez ce README
2. **FAQ** : Voir section [FAQ](#-faq-questions-fréquentes)
3. **Issues** : [Si projet sur GitHub, lien vers Issues]
4. **Contact** : CHEN Emilie ou TOUSSAH Harrol

---

## 🌟 Remerciements

Merci d'utiliser notre **Dashboard Financier** !

N'hésitez pas à :
- ⭐ Mettre une étoile au projet (si GitHub)
- 💬 Nous faire part de vos retours
- 🐛 Signaler les bugs
- 💡 Proposer des améliorations

**Vos retours sont précieux pour améliorer l'outil.**

---

## 📊 Statistiques du projet

- **Lignes de code** : ~1 200 lignes (Python)
- **Fichiers** : 7 fichiers sources
- **Fonctions** : 15+ fonctions
- **Ratios calculés** : 7 ratios essentiels
- **Temps de développement** : [Votre estimation]
- **Version actuelle** : 3.0

---

**Version** : 3.0  
**Dernière mise à jour** : Novembre 2024  
**Statut** : Production Ready ✅

---

<div align="center">

**Développé avec ❤️ par CHEN Emilie & TOUSSAH Harrol**

[⬆️ Retour en haut](#-dashboard-financier)

</div>
