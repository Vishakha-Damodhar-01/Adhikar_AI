import streamlit as st
import requests

# --- CONFIGURATION ---
DIFY_API_KEY = ""
DIFY_API_URL = "https://api.dify.ai/v1/chat-messages"

# --- UI OVERHAUL ---
st.set_page_config(page_title="AdhikarAI", page_icon="⚖️", layout="wide")

st.markdown("""
    <style>
    /* 1. RESTORED: Original Top-to-Bottom Indian Flag Gradient */
    .stApp {
        background: linear-gradient(180deg, #FF9933 0%, #FFFFFF 50%, #138808 100%);
        background-attachment: fixed;
    }

    /* 2. Glassmorphism for Left Column (Categories) */
    [data-testid="column"]:nth-child(1) {
        background: rgba(255, 255, 255, 0.25);
        backdrop-filter: blur(12px);
        border-radius: 20px;
        padding: 25px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 128, 0.1);
    }

    /* 3. High-Contrast Teal Toggle Design */
    div[data-testid="stRadio"] > div {
        gap: 12px;
    }

    div[data-testid="stRadio"] label {
        background: rgba(0, 128, 128, 0.9) !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-radius: 12px !important;
        padding: 14px 18px !important;
        transition: all 0.3s ease !important;
        box-shadow: 2px 4px 8px rgba(0,0,0,0.15);
    }

    div[data-testid="stRadio"] label:hover {
        transform: scale(1.02);
        background: #008080 !important;
        box-shadow: 4px 8px 15px rgba(0,0,0,0.2);
    }

    /* 4. Ensure White Text is readable on Teal */
    div[data-testid="stRadio"] label p {
        color: white !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        letter-spacing: 0.3px;
    }

    /* 5. Floating Message Bubbles with subtle border */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.92) !important;
        border-radius: 18px !important;
        border: 1px solid rgba(0, 128, 128, 0.15) !important;
        box-shadow: 4px 4px 12px rgba(0,0,0,0.06);
        margin-bottom: 12px;
        color: #1a1a1a !important;
    }

    /* 6. Professional Header Typography */
    .main-title {
        font-family: 'Trebuchet MS', sans-serif;
        font-weight: 800;
        color: #000080;
        margin-bottom: 0;
    }

    /* Hide redundant UI elements */
    [data-testid="collapsedControl"] { display: none; }
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- APP LAYOUT ---
# Using fixed columns for a stable layout (No sidebar collapse issues)
col_nav, col_chat = st.columns([1, 3.5], gap="medium")

with col_nav:
    st.markdown("<h2 style='color: #000080; text-align:center;'>⚖️ Categories</h2>", unsafe_allow_html=True)
    category = st.radio(
        "Focus Area",
        ["General", "Arrest Rights", "FIR Rules", "Women Safety", "Labor Laws"],
        index=0,
        label_visibility="collapsed"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.info(f"Currently Browsing: {category}")

with col_chat:
    st.markdown("<h1 class='main-title' style='text-align: center;'>AdhikarAI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #000080; font-weight: bold; font-size: 1.1rem;'>Your Digital Gateway to Legal Empowerment</p>", unsafe_allow_html=True)

    # Session Management
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat Display
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(f"<div style='color:white;'>{message['content']}</div>", unsafe_allow_html=True)

    # Chat Input
    if prompt := st.chat_input(f"Type your {category} question here..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(f"<div style='color:#000;'>{prompt}</div>", unsafe_allow_html=True)

        # RAG Logic with Dify API
        enhanced_query = f"Provide a detailed answer regarding {category}: {prompt}" if category != "General" else prompt
        headers = {"Authorization": f"Bearer {DIFY_API_KEY}", "Content-Type": "application/json"}
        payload = {"inputs": {}, "query": enhanced_query, "response_mode": "blocking", "user": "adhikar_user"}

        with st.chat_message("assistant"):
            status = st.empty()
            status.markdown("🔍 *Searching legal sections...*")
            
            try:
                response = requests.post(DIFY_API_URL, headers=headers, json=payload)
                response.raise_for_status()
                answer = response.json().get("answer", "I couldn't find a specific section for that.")
                status.markdown(f"<div style='color:#000;'>{answer}</div>", unsafe_allow_html=True)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                status.error(f"API Error: {str(e)}")