# Configuration et constantes du dashboard

# Seuils de sécurité pour chaque ratio
SEUILS_SECURITE = {
    "Marge nette": {
        "min": 0.05, 
        "optimal": 0.10, 
        "label": "5%", 
        "optimal_label": "10%"
    },
    "ROA": {
        "min": 0.05, 
        "optimal": 0.10, 
        "label": "5%", 
        "optimal_label": "10%"
    },
    "ROE": {
        "min": 0.10, 
        "optimal": 0.15, 
        "label": "10%", 
        "optimal_label": "15%"
    },
    "Liquidité générale": {
        "min": 1.0, 
        "optimal": 1.5, 
        "label": "1.0", 
        "optimal_label": "1.5"
    },
    "Liquidité immédiate": {
        "min": 0.5, 
        "optimal": 1.0, 
        "label": "0.5", 
        "optimal_label": "1.0"
    },
    "Endettement": {
        "max": 2.0, 
        "optimal": 1.0, 
        "label": "2.0", 
        "optimal_label": "1.0", 
        "inverse": True
    },
    "Autonomie financière": {
        "min": 0.3, 
        "optimal": 0.5, 
        "label": "30%", 
        "optimal_label": "50%"
    }
}

# Ratios affichés en pourcentage
RATIOS_PERCENTAGE = ["Marge nette", "ROA", "ROE", "Autonomie financière"]

# Couleurs pour les graphiques
GRAPH_COLORS = ['#667eea', '#10b981', '#ef4444', '#f59e0b', '#8b5cf6', '#ec4899', '#06b6d4']

# Couleurs pour les statuts
STATUS_COLORS = {
    "optimal": {"color": "#10b981", "border": "#059669"},
    "acceptable": {"color": "#f59e0b", "border": "#d97706"},
    "risque": {"color": "#ef4444", "border": "#dc2626"},
    "suivi": {"color": "#94a3b8", "border": "#64748b"}
}

# Données du template Excel
TEMPLATE_DATA = {
    'Année': [2020, 2021, 2022, 2023, 2024],
    'Chiffre d\'affaires': [720000, 850000, 980000, 1220000, 1340000],
    'Résultat net': [62000, 88000, 110000, 145000, 168000],
    'Actif total': [1250000, 1500000, 1750000, 2000000, 2250000],
    'Capitaux propres': [680000, 740000, 850000, 970000, 1120000],
    'Actif courant': [490000, 530000, 610000, 720000, 860000],
    'Passif courant': [340000, 410000, 440000, 520000, 610000],
    'Dettes totales': [770000, 760000, 900000, 1030000, 1130000],
    'Trésorerie': [75000, 95000, 115000, 155000, 170000],
    'Créances clients': [110000, 135000, 160000, 200000, 235000],
}
