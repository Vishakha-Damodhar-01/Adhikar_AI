# 🇮🇳 AdhikarAI: RAG-Based Legal Agentic AI

**Empowering 1.4 Billion Citizens with Digital Legal Literacy**

[Live Demo](https://your-app-link.streamlit.app) · [Dify Backend](https://dify.ai) · [Report Bug](https://github.com/Vishakha-Damodhar-01/AdhikarAI/issues)

AdhikarAI is a production-grade **RAG-based Agentic AI** designed to bridge the gap between complex legal jargon and citizen awareness. As India transitions from the IPC to the new **Bharatiya Nyaya Sanhita (BNS)** and **BNSS**, AdhikarAI acts as an autonomous legal companion—translating 1,000+ pages of legal code into simple, actionable rights.

---

## 🧠 Why RAG + Agentic AI for Law?

Traditional search engines give you links; AdhikarAI gives you answers.
*   **RAG (Retrieval-Augmented Generation):** Unlike standard AI that might hallucinate, our pipeline retrieves exact sections from the **BNS & BNSS 2023** official gazettes.
*   **Agentic Reasoning:** The system doesn't just summarize; it reasons through the user's specific context (e.g., "Am I being illegally detained?") and provides step-by-step legal procedures.
*   **Zero-Jargon Policy:** Powered by a custom-prompted LLM engine, every response is simplified to an 8th-grade reading level.

---

## 🎯 What AdhikarAI Does

| Step | Feature | Description |
| :--- | :--- | :--- |
| 📂 | **Dataset Selection** | Toggle between Women Safety, Labor Laws, FIR Rules, or General BNS. |
| 🔍 | **Semantic Search** | Uses vector embeddings to find legal meaning, not just keywords. |
| 🛡️ | **Rights Guard** | Provides immediate "Know Your Rights" checklists for police interactions. |
| 📜 | **BNS/BNSS Cross-Ref** | Automatically cites the specific New Law section for every answer. |

---

## 🤖 How the AI Works
```text
       User Asks a Legal Question
                  ↓
    Agent Identifies Category & Intent
                  ↓
    RAG Pipeline retrieves BNS/BNSS context
                  ↓
    LLM processes legal text → Simplified English
                  ↓
    UI renders response in Tricolour Interface
🚀 Features
Glassmorphism UI: A modern "Frosted Glass" interface with a stable two-column layout.

High-Contrast Toggles: Teal-blue buttons for category selection with micro-interactions.

Context-Aware Prompting: The AI "knows" if you are a victim, a student, or a concerned citizen based on your query.

Indian Flag Aesthetic: A respectful, professional design language reflecting the project's national mission.

🛠️ Tech Stack
Backend & AI

Dify.ai: For RAG orchestration and Knowledge Base management.

BNS/BNSS Datasets: Official 2023 Indian Legal Gazettes.

Python: Core logic and API integration.

Frontend

Streamlit: For a fast, responsive, and data-focused UI.

Custom CSS: For the radiant tricolour background and Glassmorphism.

⚙️ Setup & Installation
1. Clone the Repo
Bash
git clone [https://github.com/Vishakha-Damodhar-01/AdhikarAI.git](https://github.com/Vishakha-Damodhar-01/AdhikarAI.git)
cd AdhikarAI
2. Install Dependencies
Bash
pip install -r requirements.txt
3. Configure API
Create a .streamlit/secrets.toml or edit app.py:

Python
DIFY_API_KEY = "your_dify_secret_key"
4. Run App
Bash
streamlit run app.py
🔮 Future Scope
🗣️ Voice Support: STT (Speech-to-Text) for non-literate users.

🌍 Vernacular AI: Native support for Hindi, Marathi, and Tamil.

📱 WhatsApp Integration: A legal bot for easy access in rural areas.

⚖️ License
Distributed under the MIT License. See LICENSE for more information.

Built with 🇮🇳 by Vishakha for the Digital India Vision.


### Why this is better:
1.  **The Hook:** It defines the project's mission ("Empowering 1.4 Billion Citizens") immediately.
2.  **Skimmability:** Tables and bullet points make it easy for a judge to see your tech stack and features.
3.  **Modern Feel:** The use of emojis (🧠, 🎯, 🤖) and the "How it Works" flow makes it look like a high-end AI tool.

Go ahead and paste this into your `README.md`. It’s going to make a massive differen
