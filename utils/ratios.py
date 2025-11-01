import pandas as pd

def calculer_ratios(df):
    required_cols = [
        "Année", "Chiffre d'affaires", "Résultat net", "Actif total",
        "Capitaux propres", "Actif courant", "Passif courant",
        "Dettes totales", "Trésorerie", "Créances clients"
    ]

    if not all(col in df.columns for col in required_cols):
        raise ValueError(f"Les colonnes requises sont manquantes. Il faut : {required_cols}")

    ratios = pd.DataFrame()
    ratios["Année"] = df["Année"]
    ratios["Marge nette"] = df["Résultat net"] / df["Chiffre d'affaires"]
    ratios["ROA"] = df["Résultat net"] / df["Actif total"]
    ratios["ROE"] = df["Résultat net"] / df["Capitaux propres"]
    ratios["Liquidité générale"] = df["Actif courant"] / df["Passif courant"]
    ratios["Liquidité immédiate"] = (df["Trésorerie"] + df["Créances clients"]) / df["Passif courant"]
    ratios["Endettement"] = df["Dettes totales"] / df["Capitaux propres"]
    ratios["Autonomie financière"] = df["Capitaux propres"] / df["Actif total"]

    return ratios
