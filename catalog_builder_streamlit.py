# ... existing code ...
# Configurazione della pagina Streamlit per un look moderno e ampio
st.set_page_config(
    page_title="Catalogo & Schede",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Stile CSS personalizzato per allineare l'estetica di Streamlit con la nostra griglia scura e forzare i testi a bianco
st.markdown("""
<style>
    /* Sfondo generale e toni scuri */
    .stApp {
        background-color: #0f172a;
        color: #ffffff !important;
    }
    /* Forza il testo bianco per intestazioni, label e paragrafi standard di Streamlit */
    h1, h2, h3, h4, h5, h6, p, span, label, li {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif;
    }
    /* Personalizzazione estetica dei campi di input (Testi a bianco) */
    .stTextInput input, .stTextArea textarea, [data-baseweb="select"] {
        color: #ffffff !important;
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #6366f1 !important;
        box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2) !important;
    }
    /* Forza i segnaposto (placeholder) in bianco opaco / semi-trasparente */
    .stTextInput input::placeholder, .stTextArea textarea::placeholder, input::placeholder, textarea::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
        opacity: 1 !important; /* Firefox */
    }
    /* Personalizzazione dei menu a tendina (Dropdown / Popover) */
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #1e293b !important;
        border: 1px solid #334155 !important;
        border-radius: 8px !important;
    }
    /* Singole opzioni dentro il menu a tendina */
    div[role="option"], li[role="option"], [data-baseweb="menu"] [role="option"], [data-baseweb="popover"] [role="option"] {
        background-color: #1e293b !important;
        color: #ffffff !important;
        padding: 8px 12px !important;
        transition: background-color 0.2s ease !important;
    }
    /* Hover sulle opzioni del dropdown */
    div[role="option"]:hover, li[role="option"]:hover, [role="option"][aria-selected="true"] {
        background-color: #334155 !important;
        color: #ffffff !important;
    }
    /* Testo selezionato nel dropdown */
    div[data-baseweb="select"] div {
        color: #ffffff !important;
    }
    /* Pulsanti personalizzati */
    div.stButton > button {
        background-color: #4f46e5 !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.5rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        background-color: #4338ca !important;
        box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.3) !important;
        transform: translateY(-2px);
    }
    /* Footer personalizzato */
    .custom-footer {
        margin-top: 5rem;
        padding-top: 2rem;
        border-top: 1px solid #1e293b;
        text-align: center;
        font-size: 0.8rem;
        color: #94a3b8;
    }
    .custom-footer a {
        color: #818cf8;
        text-decoration: none;
        font-weight: 500;
    }
    .custom-footer a:hover {
        text-decoration: underline;
    }
</style>
""", unsafe_allow_html=True)

# Dizionario locale ad associazione ASIN per i prodotti noti (fallback di sicurezza anti-CAPTCHA)
# ... existing code ...
# Header principale dell'applicazione
st.title("Catalogo & Schede")

col_add, col_clean = st.columns([5, 1])

with col_add:
    # Campo di inserimento a singola riga
    singolo_link = st.text_input("Aggiungi un singolo link Amazon.it:", placeholder="Incolla qui il link del prodotto...")
    if singolo_link.strip():
        asin = estrai_asin(singolo_link)
# ... existing code ...