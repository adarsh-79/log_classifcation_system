
# 🔍 Log Classification System

A hybrid log classification system that categorizes log messages using three different techniques: **Regex-based rules**, **SBERT-based semantic similarity**, and **LLM-based classification (LLaMA-3.1)**. This layered system is designed for flexibility, precision, and extensibility in production environments.

---

## 📁 Project Structure (Updated)

```text
log_classification_system/
│
├── config/                   
│   └── .env                 # API key
│
├── dataset/
│   └── synthetic_logs.csv   # Sample or synthetic logs for testing/training
│
├── model/                   # Core ML classification logic lives here
│   ├── classify_regex.py     # Rule-based (regex) classifier
│   ├── classify_sbert.py     # SBERT + SVC classifier
│   ├── classify.py           # Combines regex, SBERT, and LLM
│   ├── classiy_llm.py        # LLaMA-3.1 (via Groq API) classifier
│   ├── regex_patterns.py     # List of regex patterns and their categories
│   ├── svc.joblib            # Pre-trained SVC model
│   └── training.ipynb        # Notebook for training the SBERT + SVC model
│
├── schema/                   # pydantic schema for user input
│   └── user_input.py 
│   
├── api.py                  # Backend API endpoint for classification
├── frontend.html           # Simple front-end UI 
├── README.md               # Project documentation
├── requirements.txt        # List of Python package dependencies
```

---

## 🧠 How It Works

1. **Regex Rules**:
   - Fast and interpretable.
   - Checks if the log matches any known patterns (e.g., backup completion, HTTP errors, security alerts).
   - Returns early if a pattern matches.

2. **SBERT + SVC**:
   - Embeds the log message using `all-MiniLM-L6-v2`.
   - Classifies using a trained `SVC` model.
   - Used only if the log source is **not `LegacyCRM`**.

3. **LLM (LLaMA 3.1 via Groq)**:
   - Final fallback method.
   - Handles ambiguous, novel, or unstructured logs.
   - Returns a structured category or `Unclassified`.



## ⚙️ Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file under `config/`:

```ini
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Load or Train the SVC Model

Load `model/svc.joblib` from the model directory.

---

## 🧩 Trained Categories

- Workflow Error  
- Deprecation Warning  
- HTTP Status  
- Critical Error  
- Security Alert  
- Error  
- System Notification  
- Resource Usage  
- User Action  
- Unclassified

---

## 📌 Notes

- The model is trained on a synthetic log dataset
- The fallback to LLM ensures resilience for previously unseen or noisy logs.
- Regex logic handles specific patterns efficiently.
- SBERT-based classifier can be fine-tuned for domain-specific logs.

---

## 📜 License

MIT License