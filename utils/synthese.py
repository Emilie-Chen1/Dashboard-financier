import streamlit as st

def afficher_synthese(ratios_df, SEUILS_SECURITE, RATIOS_PERCENTAGE, STATUS_COLORS):
    """
    Affiche la section "Synthèse de l'analyse" avec expanders
    
    Args:
        ratios_df: DataFrame contenant les ratios calculés
        SEUILS_SECURITE: Dictionnaire des seuils de sécurité
        RATIOS_PERCENTAGE: Liste des ratios affichés en pourcentage
        STATUS_COLORS: Dictionnaire des couleurs par statut
    """
    
    st.subheader("📊 Synthèse de l'analyse")
    
    # Classifier tous les ratios
    ratios_optimaux = []
    ratios_acceptables = []
    ratios_risque = []
    annees_alertes = {}  # Dictionnaire pour compter les alertes par année
    
    for ratio in [c for c in ratios_df.columns if c != "Année"]:
        if ratio in SEUILS_SECURITE:
            config = SEUILS_SECURITE[ratio]
            valeur_actuelle = ratios_df[ratio].iloc[-1]
            
            # Analyser chaque année pour ce ratio
            details_annees = []
            nb_hors_seuil = 0
            
            for i in range(len(ratios_df)):
                annee = int(ratios_df["Année"].iloc[i])
                valeur = ratios_df[ratio].iloc[i]
                
                # Déterminer le statut pour cette année
                if "inverse" in config and config["inverse"]:
                    if valeur <= config["optimal"]:
                        statut_annee = "optimal"
                        icon = "✅"
                    elif valeur <= config["max"]:
                        statut_annee = "acceptable"
                        icon = "⚠️"
                    else:
                        statut_annee = "risque"
                        icon = "🚨"
                        nb_hors_seuil += 1
                        annees_alertes[annee] = annees_alertes.get(annee, 0) + 1
                else:
                    if valeur >= config["optimal"]:
                        statut_annee = "optimal"
                        icon = "✅"
                    elif valeur >= config["min"]:
                        statut_annee = "acceptable"
                        icon = "⚠️"
                    else:
                        statut_annee = "risque"
                        icon = "🚨"
                        nb_hors_seuil += 1
                        annees_alertes[annee] = annees_alertes.get(annee, 0) + 1
                
                # Formater la valeur
                if ratio in RATIOS_PERCENTAGE:
                    valeur_str = f"{valeur*100:.1f}%"
                else:
                    valeur_str = f"{valeur:.2f}"
                
                details_annees.append({
                    "annee": annee,
                    "valeur": valeur_str,
                    "statut": statut_annee,
                    "icon": icon
                })
            
            # Déterminer la catégorie du ratio (basée sur la valeur actuelle)
            if "inverse" in config and config["inverse"]:
                if valeur_actuelle <= config["optimal"]:
                    categorie = "optimal"
                elif valeur_actuelle <= config["max"]:
                    categorie = "acceptable"
                else:
                    categorie = "risque"
            else:
                if valeur_actuelle >= config["optimal"]:
                    categorie = "optimal"
                elif valeur_actuelle >= config["min"]:
                    categorie = "acceptable"
                else:
                    categorie = "risque"
            
            # Formater la valeur actuelle
            if ratio in RATIOS_PERCENTAGE:
                valeur_actuelle_str = f"{valeur_actuelle*100:.1f}%"
            else:
                valeur_actuelle_str = f"{valeur_actuelle:.2f}"
            
            ratio_info = {
                "nom": ratio,
                "valeur_actuelle": valeur_actuelle_str,
                "details_annees": details_annees,
                "nb_hors_seuil": nb_hors_seuil
            }
            
            if categorie == "optimal":
                ratios_optimaux.append(ratio_info)
            elif categorie == "acceptable":
                ratios_acceptables.append(ratio_info)
            else:
                ratios_risque.append(ratio_info)
    
    # Afficher les métriques générales
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("✅ Ratios optimaux", f"{len(ratios_optimaux)}/7")
    with col2:
        st.metric("⚠️ Ratios acceptables", f"{len(ratios_acceptables)}/7")
    with col3:
        st.metric("🚨 Ratios en risque", f"{len(ratios_risque)}/7")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # --- RATIOS OPTIMAUX ---
    with st.expander(f"✅ **Ratios optimaux ({len(ratios_optimaux)}/7)** - Voir le détail", expanded=False):
        if ratios_optimaux:
            for ratio_info in ratios_optimaux:
                st.markdown(f"**{ratio_info['nom']}** : {ratio_info['valeur_actuelle']}")
                
                # Créer le tableau des années
                cols_annees = st.columns(len(ratio_info['details_annees']))
                for idx, detail in enumerate(ratio_info['details_annees']):
                    with cols_annees[idx]:
                        st.markdown(f"""
                        <div style='text-align: center; padding: 8px; background-color: #1e293b; border-radius: 4px; margin: 4px 0;'>
                            <div style='font-size: 0.85em; color: #94a3b8;'>{detail['annee']}</div>
                            <div style='font-size: 1.1em; color: #e2e8f0; font-weight: bold;'>{detail['valeur']}</div>
                            <div style='font-size: 1.2em;'>{detail['icon']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("---")
        else:
            st.info("Aucun ratio optimal pour le moment.")
    
    # --- RATIOS ACCEPTABLES ---
    with st.expander(f"⚠️ **Ratios acceptables ({len(ratios_acceptables)}/7)** - Voir le détail", expanded=True):
        if ratios_acceptables:
            for ratio_info in ratios_acceptables:
                st.markdown(f"**{ratio_info['nom']}** : {ratio_info['valeur_actuelle']}")
                
                if ratio_info['nb_hors_seuil'] > 0:
                    st.warning(f"⚠️ {ratio_info['nb_hors_seuil']} année(s) hors seuil minimum")
                
                # Créer le tableau des années
                cols_annees = st.columns(len(ratio_info['details_annees']))
                for idx, detail in enumerate(ratio_info['details_annees']):
                    with cols_annees[idx]:
                        # Couleur de fond selon le statut
                        if detail['statut'] == 'risque':
                            bg_color = '#7f1d1d'
                        elif detail['statut'] == 'acceptable':
                            bg_color = '#78350f'
                        else:
                            bg_color = '#1e293b'
                        
                        st.markdown(f"""
                        <div style='text-align: center; padding: 8px; background-color: {bg_color}; border-radius: 4px; margin: 4px 0;'>
                            <div style='font-size: 0.85em; color: #94a3b8;'>{detail['annee']}</div>
                            <div style='font-size: 1.1em; color: #e2e8f0; font-weight: bold;'>{detail['valeur']}</div>
                            <div style='font-size: 1.2em;'>{detail['icon']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("---")
        else:
            st.success("Aucun ratio acceptable, tous sont optimaux !")
    
    # --- RATIOS EN RISQUE ---
    with st.expander(f"🚨 **Ratios en risque ({len(ratios_risque)}/7)** - Voir le détail", expanded=True):
        if ratios_risque:
            for ratio_info in ratios_risque:
                st.markdown(f"**{ratio_info['nom']}** : {ratio_info['valeur_actuelle']}")
                
                st.error(f"🚨 Attention : {ratio_info['nb_hors_seuil']} année(s) hors seuil")
                
                # Créer le tableau des années
                cols_annees = st.columns(len(ratio_info['details_annees']))
                for idx, detail in enumerate(ratio_info['details_annees']):
                    with cols_annees[idx]:
                        # Couleur de fond selon le statut
                        if detail['statut'] == 'risque':
                            bg_color = '#7f1d1d'
                        elif detail['statut'] == 'acceptable':
                            bg_color = '#78350f'
                        else:
                            bg_color = '#1e293b'
                        
                        st.markdown(f"""
                        <div style='text-align: center; padding: 8px; background-color: {bg_color}; border-radius: 4px; margin: 4px 0;'>
                            <div style='font-size: 0.85em; color: #94a3b8;'>{detail['annee']}</div>
                            <div style='font-size: 1.1em; color: #e2e8f0; font-weight: bold;'>{detail['valeur']}</div>
                            <div style='font-size: 1.2em;'>{detail['icon']}</div>
                        </div>
                        """, unsafe_allow_html=True)
                
                st.markdown("---")
        else:
            st.success("🎉 Excellent ! Aucun ratio en risque.")