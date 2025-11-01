# Styles CSS personnalisés pour le dashboard

CUSTOM_CSS = """
    <style>
    .main { padding: 0rem 1rem; }
    .stMetric {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 20px; border-radius: 15px; border: 1px solid #475569;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    }
    .stMetric label { color: #94a3b8 !important; font-weight: 600; }
    .stMetric [data-testid="stMetricValue"] { color: #e2e8f0 !important; font-size: 1.8rem !important; }
    h1 { color: #f1f5f9; font-weight: 700; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }
    h2 { color: #e2e8f0; font-weight: 600; margin-top: 2rem; border-bottom: 2px solid #475569; padding-bottom: 0.5rem; }
    h3 { color: #cbd5e1; font-weight: 500; }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white; border-radius: 10px; padding: 0.6rem 2rem; border: none; font-weight: 600;
        box-shadow: 0 4px 6px rgba(102, 126, 234, 0.3); transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
        box-shadow: 0 6px 12px rgba(102, 126, 234, 0.5); transform: translateY(-2px);
    }
    div[data-testid="stExpander"] {
        background-color: #1e293b; border-radius: 12px; border: 1px solid #475569;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px; background-color: #1e293b; border-radius: 10px; padding: 5px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #334155; border-radius: 8px; color: #94a3b8; padding: 10px 20px; font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white;
    }
    .trend-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 15px; border-radius: 12px; margin: 10px 0; border: 1px solid #475569;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 50px; border-radius: 20px; color: white; margin: 20px 0;
        box-shadow: 0 8px 16px rgba(102, 126, 234, 0.4);
    }
    .metric-card {
        background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
        padding: 20px; border-radius: 15px; border: 1px solid #475569;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3); margin: 10px 0;
    }
    hr { border-color: #475569; margin: 2rem 0; }
    </style>
    """