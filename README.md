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

---

## 🤖 How the AI Works
##

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
```
---

## 🚀 Features
---

## 🚀 Key Features

*   **🧠 RAG-Powered Accuracy:** Unlike standard AI, our pipeline retrieves exact sections from the official **BNS & BNSS 2023** gazettes to prevent hallucinations.
*   **🤖 Agentic Reasoning:** The system doesn't just summarize; it autonomously reasons through your specific context (e.g., "Am I being illegally detained?") to provide step-by-step legal procedures.
*   **⚖️ Zero-Jargon Policy:** Every response is processed by a custom-prompted LLM engine to simplify complex legal terms into an 8th-grade reading level.
*   **🇮🇳 Tricolour Glassmorphism UI:** A premium, modern interface designed with an Indian flag aesthetic, featuring frosted glass effects and high-contrast toggles.
*   **📂 Specialized Dataset Toggles:** Users can specifically target their queries toward **Women Safety**, **Labor Laws**, **FIR Rules**, or **Arrest Rights**.

---  
---

## 🛠️ Tech Stack

### Backend & AI
*   **Dify.ai:** Used for RAG orchestration and seamless Knowledge Base management.
*   **BNS/BNSS Datasets:** Grounded in the official 2023 Indian Legal Gazettes for high accuracy.
*   **Python:** Powers the core logic, API handling, and data processing.

### Frontend
*   **Streamlit:** Provides a fast, responsive, and data-focused user interface.
*   **Custom CSS:** Implements the radiant tricolour background and premium Glassmorphism effects.

---

## ⚙️ Setup & Installation

### 1. Clone the Repo
```bash
git clone [https://github.com/Vishakha-Damodhar-01/AdhikarAI.git](https://github.com/Vishakha-Damodhar-01/AdhikarAI.git)
cd AdhikarAI
```

----
### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

----
### 3. Configure API Key
Open app.py and replace the placeholder with your Dify Secret Key:
```bash
DIFY_API_KEY = "YOUR_SECRET_API_KEY_HERE"
```
---
### 4. Run the Application
```bash
streamlit run app.py
```

---
## 📜 Future Scope
*  **🗣️ Voice Support:** Implementing Speech-to-Text (STT) functionality for non-literate or visually impaired users.
* **🌍 Vernacular AI:** Expanding native support for Hindi, Marathi, and other regional languages.
*  **📱 WhatsApp Integration:** Developing a lightweight legal bot for easy access in rural areas via WhatsApp API.

---
## ⚖️ License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
