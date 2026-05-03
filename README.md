# 🇮🇳 AdhikarAI: AI-Powered Legal Rights Companion

**AdhikarAI** is an intelligent legal literacy platform designed to help Indian citizens navigate the transition to the new **Bharatiya Nyaya Sanhita (BNS)** and **Bharatiya Nagarik Suraksha Sanhita (BNSS)** laws. 

---

## 🚀 Key Features
*   **Dataset Toggles:** Specifically target queries toward **Women Safety**, **Labor Laws**, **FIR Rules**, or **Arrest Rights**.
*   **RAG Architecture:** Retrieval-Augmented Generation ensures answers are grounded in official legal documents.
*   **Premium UI:** A high-contrast, Indian Flag-themed interface with Glassmorphism effects and teal-blue toggles.
*   **Contextual Intelligence:** The AI automatically adapts its search based on the category you select.

---

## 🧠 Technical Architecture

### 1. The AI Agent (Dify.ai)
*   **Knowledge Base:** Created by indexing the official PDFs of the BNS and BNSS 2023 acts.
*   **Orchestration:** Built using a Dify Chatflow to handle complex legal reasoning.
*   **API:** Exposed via a secure REST API to communicate with our custom Python frontend.

### 2. The Frontend (Streamlit)
*   **Layout:** A stable two-column layout that prevents UI shifting.
*   **Styling:** Custom CSS injection for the tricolour gradient and "Frosted Glass" navigation bar.

---

## 🛠️ Installation & Setup

Follow these steps to run AdhikarAI on your local machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/AdhikarAI.git](https://github.com/YOUR_USERNAME/AdhikarAI.git)
cd AdhikarAI

### 2. Install Dependencies
To install the necessary libraries, run the following command in your terminal:
```bash
pip install -r requirements.txt

### 3. Set Up API Key
Open the `app.py` file in your code editor and replace the placeholder text with your actual Dify Secret Key:
```python
DIFY_API_KEY = "YOUR_SECRET_API_KEY_HERE"


### 4. Run the Application
Once the API key is set, launch the application by running this command in your terminal:

```bash
streamlit run app.py

🌐 Deployment
This project is optimized for deployment on Streamlit Community Cloud.

Push your code to a GitHub repository.

Connect the repository to Streamlit Cloud.

Add your DIFY_API_KEY to the Advanced Settings > Secrets to keep your credentials secure.

📜 Future Scope
Multilingual Support: Expanding to Hindi, Marathi, and other regional languages.

Voice Integration: Allowing users to ask questions via voice for better accessibility.

Offline Mode: A lightweight version for areas with low internet connectivity.

## ⚖️ License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.