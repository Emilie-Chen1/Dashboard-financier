import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import io
import numpy as np
from utils.ratios import calculer_ratios
from utils.synthese import afficher_synthese
from config import SEUILS_SECURITE, RATIOS_PERCENTAGE, GRAPH_COLORS, STATUS_COLORS, TEMPLATE_DATA
from styles import CUSTOM_CSS

# --- CONFIG GLOBALE ---
st.set_page_config(
    page_title="Dashboard Financier", 
    layout="wide", 
    page_icon="💹",
    initial_sidebar_state="collapsed"
)

# Appliquer les styles CSS
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- HEADER ---
st.title("💹 Dashboard de Performance Financière")
st.markdown("**Analyse complète et interactive de vos indicateurs financiers**")

st.markdown("---")

# --- UPLOAD DU FICHIER ---
st.subheader("📂 Import des données")
uploaded_file = st.file_uploader(
    "Glissez-déposez votre fichier financier ici", 
    type=["xlsx"],
    help="Format accepté : Excel (.xlsx)"
)

# Bouton de téléchargement du template
col_template1, col_template2, col_template3 = st.columns([1, 2, 1])
with col_template2:
    df_template = pd.DataFrame(TEMPLATE_DATA)
    template_buffer = io.BytesIO()
    df_template.to_excel(template_buffer, index=False, engine='openpyxl')
    template_buffer.seek(0)
    
    st.download_button(
        label="📥 Télécharger le template Excel",
        data=template_buffer,
        file_name="template_finances.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        help="Téléchargez ce fichier exemple pour voir le format attendu",
        use_container_width=True
    )
    st.caption("👆 Fichier pré-formaté avec 5 années d'exemple")

if uploaded_file:
    try:
        # Lecture du fichier Excel
        df = pd.read_excel(uploaded_file)

        # Nettoyage colonnes
        df.columns = (
            df.columns.str.strip()
            .str.replace("'", "'")
            .str.replace("'", "'")
            .str.normalize("NFKC")
        )

        # Conversion des valeurs numériques
        for col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].astype(str).str.replace(",", "").str.replace(" ", "")
                df[col] = pd.to_numeric(df[col], errors="ignore")

        # --- APERÇU DONNÉES ---
        with st.expander("📋 Aperçu des données importées", expanded=False):
            st.dataframe(df, use_container_width=True, height=200)

        # --- CALCUL DES RATIOS ---
        ratios_df = calculer_ratios(df)
        ratios_df["Année"] = ratios_df["Année"].astype(int)
        df["Année"] = df["Année"].astype(int)
        ratios_df = ratios_df.sort_values("Année")
        
        st.success("✅ Données analysées avec succès !")
        st.markdown("---")

        # --- KPI PRINCIPAUX AVEC ÉVOLUTION MOYENNE ANNUELLE ---
        st.subheader("📊 Vue d'ensemble - Indicateurs clés")
        
        ca_final = df["Chiffre d'affaires"].iloc[-1]
        rn_final = df["Résultat net"].iloc[-1]
        roe_final = ratios_df["ROE"].iloc[-1]
        
        col1, col2, col3, col4 = st.columns(4)
        
        if len(df) >= 2:
            ca_initial = df["Chiffre d'affaires"].iloc[0]
            rn_initial = df["Résultat net"].iloc[0]
            roe_initial = ratios_df["ROE"].iloc[0]
            endettement_final = ratios_df["Endettement"].iloc[-1]
            
            # Calculer le nombre d'années
            nb_annees = len(df) - 1  # Nombre de périodes de transition
            
            # Calcul du TCAM (Taux de Croissance Annuel Moyen) = CAGR
            # Formule : ((Valeur finale / Valeur initiale)^(1/n)) - 1
            if ca_initial > 0:
                ca_cagr = ((ca_final / ca_initial) ** (1 / nb_annees)) - 1
            else:
                ca_cagr = 0
            
            if rn_initial > 0:
                rn_cagr = ((rn_final / rn_initial) ** (1 / nb_annees)) - 1
            else:
                rn_cagr = 0
            
            # Pour le ROE (en points de pourcentage), on calcule la variation moyenne annuelle
            roe_variation_moyenne = (roe_final - roe_initial) / nb_annees * 100
            
            # Pour l'endettement, calculer la variation moyenne annuelle
            endettement_initial = ratios_df["Endettement"].iloc[0]
            endettement_variation_moyenne = (endettement_final - endettement_initial) / nb_annees
            
            with col1:
                # Calcul de la variation moyenne en valeur absolue
                ca_variation_valeur = (ca_final - ca_initial) / nb_annees
                st.metric(
                    "💰 Chiffre d'affaires", 
                    f"{ca_final:,.0f} €".replace(",", " "), 
                    f"{ca_cagr:+.1%} /an",
                    help=f"Évolution moyenne annuelle sur {nb_annees} an(s)"
                )
                st.caption(f"📊 {ca_variation_valeur:+,.0f} €/an".replace(",", " "))
            with col2:
                # Calcul de la variation moyenne en valeur absolue
                rn_variation_valeur = (rn_final - rn_initial) / nb_annees
                st.metric(
                    "📈 Résultat net", 
                    f"{rn_final:,.0f} €".replace(",", " "), 
                    f"{rn_cagr:+.1%} /an",
                    help=f"Évolution moyenne annuelle sur {nb_annees} an(s)"
                )
                st.caption(f"📊 {rn_variation_valeur:+,.0f} €/an".replace(",", " "))
            with col3:
                st.metric(
                    "🎯 ROE", 
                    f"{roe_final*100:.1f}%", 
                    f"{roe_variation_moyenne:+.1f} pts/an",
                    help=f"Variation moyenne annuelle sur {nb_annees} an(s)"
                )
            with col4:
                st.metric(
                    "⚖️ Endettement", 
                    f"{endettement_final:.2f}",
                    f"{endettement_variation_moyenne:+.2f} /an",
                    delta_color="inverse",
                    help=f"Variation moyenne annuelle sur {nb_annees} an(s)"
                )
        else:
            with col1:
                st.metric("💰 Chiffre d'affaires", f"{ca_final:,.0f} €".replace(",", " "))
            with col2:
                st.metric("📈 Résultat net", f"{rn_final:,.0f} €".replace(",", " "))
            with col3:
                st.metric("🎯 ROE", f"{roe_final*100:.1f}%")
            with col4:
                st.metric("⚖️ Endettement", f"{ratios_df['Endettement'].iloc[-1]:.2f}")

        st.markdown("---")

        # --- GRAPHIQUE INTERACTIF ET TABLEAU ---
        st.subheader("📊 Analyse des ratios financiers")
        
        view_mode = st.radio(
            "Affichage",
            ["📈 Graphique d'évolution", "📋 Tableau récapitulatif"],
            horizontal=True,
            label_visibility="collapsed"
        )
        
        if view_mode == "📈 Graphique d'évolution":
            selected_ratios = st.multiselect(
                "📌 Sélectionnez les ratios à afficher :",
                options=[c for c in ratios_df.columns if c != "Année"],
                default=["Marge nette", "ROE", "Endettement"],
                help="Vous pouvez sélectionner plusieurs ratios pour les comparer"
            )

            if selected_ratios:
                ratios_plot = ratios_df.copy()
                ratios_plot["Année"] = ratios_plot["Année"].astype(str)
                
                fig = go.Figure()
                
                for idx, ratio in enumerate(selected_ratios):
                    if ratio in RATIOS_PERCENTAGE:
                        y_values = (ratios_plot[ratio] * 100).tolist()
                    else:
                        y_values = ratios_plot[ratio].tolist()
                    
                    # Calculer l'évolution par rapport à l'année précédente (N vs N-1)
                    y_values_evolution = [0]  # Première année = 0% (pas de comparaison)
                    
                    for i in range(1, len(y_values)):
                        val_precedente = y_values[i-1]
                        val_actuelle = y_values[i]
                        
                        if val_precedente != 0:
                            evolution = ((val_actuelle - val_precedente) / abs(val_precedente)) * 100
                        else:
                            evolution = 0
                        
                        y_values_evolution.append(evolution)
                    
                    fig.add_trace(go.Scatter(
                        x=ratios_plot["Année"].tolist(),
                        y=y_values_evolution,
                        name=ratio,
                        mode='lines+markers',
                        line=dict(width=3, color=GRAPH_COLORS[idx % len(GRAPH_COLORS)]),
                        marker=dict(size=10),
                        hovertemplate='<b>%{fullData.name}</b><br>Année: %{x}<br>Évolution: %{y:+.1f}%<extra></extra>'
                    ))
                
                fig.add_hline(y=0, line_dash="dash", line_color="#94a3b8", line_width=2,
                             annotation_text="Stabilité", annotation_position="right",
                             annotation_font_color="#94a3b8", annotation_font_size=12)
                
                fig.update_layout(
                    height=500,
                    template="plotly_dark",
                    hovermode="x unified",
                    legend=dict(
                        orientation="h",
                        yanchor="bottom",
                        y=1.02,
                        xanchor="right",
                        x=1,
                        bgcolor='rgba(30, 41, 59, 0.8)',
                        bordercolor='#475569',
                        borderwidth=1
                    ),
                    font=dict(size=12, color='#e2e8f0'),
                    xaxis_title="Année",
                    yaxis_title="Évolution par rapport à l'année précédente (%)",
                    plot_bgcolor='#0f172a',
                    paper_bgcolor='rgba(0,0,0,0)',
                    xaxis=dict(gridcolor='#334155'),
                    yaxis=dict(gridcolor='#334155', zeroline=True, zerolinecolor='#94a3b8', zerolinewidth=2)
                )
                
                fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#334155')
                fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#334155')
                st.plotly_chart(fig, use_container_width=True)
                
                st.success("📊 **Lecture du graphique** : Les valeurs affichent le % de variation par rapport à l'année précédente (N vs N-1). Par exemple, +15% en 2023 signifie que le ratio a augmenté de 15% entre 2022 et 2023.")
            else:
                st.info("👆 Sélectionnez au moins un ratio pour afficher le graphique")
        
        else:
            # Tableau récapitulatif avec couleurs selon tendance
            def color_by_trend(s):
                """Applique une couleur selon la tendance par rapport à l'année précédente"""
                if s.name == "Année":
                    return [''] * len(s)
                
                colors = []
                for i in range(len(s)):
                    if i == 0:
                        # Première année : pas de comparaison
                        colors.append('background-color: #1e293b')
                    else:
                        val_actuelle = s.iloc[i]
                        val_precedente = s.iloc[i-1]
                        
                        # Déterminer si c'est un ratio "inverse" (endettement)
                        is_inverse = s.name == "Endettement"
                        
                        # Calculer la variation
                        if val_precedente != 0:
                            variation = ((val_actuelle - val_precedente) / abs(val_precedente))
                        else:
                            variation = 0
                        
                        # Appliquer les couleurs selon la tendance
                        if abs(variation) < 0.01:  # Stagnation (< 1% de variation)
                            colors.append('background-color: #64748b')
                        elif is_inverse:
                            # Pour l'endettement, la baisse est bonne
                            if variation < 0:
                                colors.append('background-color: #059669')  # Vert (amélioration)
                            else:
                                colors.append('background-color: #dc2626')  # Rouge (dégradation)
                        else:
                            # Pour les autres ratios, la hausse est bonne
                            if variation > 0:
                                colors.append('background-color: #059669')  # Vert (amélioration)
                            else:
                                colors.append('background-color: #dc2626')  # Rouge (dégradation)
                
                return colors
            
            # Appliquer le style
            styled_ratios = ratios_df.style.format({
                col: "{:.2%}" if col in RATIOS_PERCENTAGE else "{:.2f}"
                for col in ratios_df.columns if col != "Année"
            }).apply(color_by_trend, axis=0)
            
            st.dataframe(styled_ratios, use_container_width=True, height=300)
            
            # Légende
            col_leg1, col_leg2, col_leg3, col_leg4 = st.columns(4)
            with col_leg1:
                st.markdown("🟢 **Amélioration** par rapport à l'année N-1")
            with col_leg2:
                st.markdown("🔴 **Dégradation** par rapport à l'année N-1")
            with col_leg3:
                st.markdown("⚪ **Stagnation** (< 1% de variation)")
            with col_leg4:
                st.markdown("⚫ **Année de référence** (pas de comparaison)")

        st.markdown("---")

        # --- SYNTHÈSE DE L'ANALYSE ---
        afficher_synthese(ratios_df, SEUILS_SECURITE, RATIOS_PERCENTAGE, STATUS_COLORS)


    except Exception as e:
        st.error(f"❌ **Erreur lors du traitement du fichier**")
        st.exception(e)
        st.info("💡 Vérifiez que votre fichier contient toutes les colonnes requises")

else:
    # --- PAGE D'ACCUEIL ---
    st.markdown("""
    <div class="hero-section" style='text-align: center;'>
        <h2 style='color: white; margin-bottom: 20px;'>🚀 Bienvenue sur votre Dashboard Financier</h2>
        <p style='font-size: 1.1em; margin-bottom: 30px;'>
            Analysez vos performances financières en quelques clics
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #e2e8f0;'>📊 Analyse complète</h3>
            <ul style='color: #94a3b8;'>
                <li>Calcul automatique de 7 ratios clés</li>
                <li>Visualisations interactives</li>
                <li>Tendances et évolutions</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #e2e8f0;'>🎯 Options avancées</h3>
            <ul style='color: #94a3b8;'>
                <li>Graphique d'évolution en %</li>
                <li>Seuils de sécurité</li>
                <li>Alertes automatiques</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3 style='color: #e2e8f0;'>🎨 Interface moderne</h3>
            <ul style='color: #94a3b8;'>
                <li>Design adapté mode sombre</li>
                <li>Graphiques interactifs</li>
                <li>Navigation intuitive</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.info("👆 **Pour commencer** : Importez votre fichier de données financières en haut de la page")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #94a3b8; padding: 20px;'>
    <p>Dashboard Financier | Développé par CHEN Emilie et TOUSSAH Harrol dans le cadre du DU SDA</p>
</div>
""", unsafe_allow_html=True)