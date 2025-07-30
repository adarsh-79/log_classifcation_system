import joblib
from sentence_transformers import SentenceTransformer
import numpy as np

svc = joblib.load("model/svc.joblib")

def classify_with_sbert(log_msg: str):
    model = SentenceTransformer("all-MiniLM-L6-v2")    
    embeddings = model.encode(log_msg).reshape(1, -1)
    max_probability = np.round(np.max(svc.predict_proba(embeddings), axis=1), 2)
    

    if max_probability > 0.53:
        predicted_class = svc.predict(embeddings)
        return predicted_class[0]
    