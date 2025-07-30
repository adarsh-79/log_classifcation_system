from model.classify_regex import classify_with_regex
from model.classify_sbert import classify_with_sbert
from model.classiy_llm import classify_with_llm

def classify_log(log_msg_dict: dict):
    log_message = log_msg_dict["log_message"]
    source = log_msg_dict["source"]

    regex_predicted_class = classify_with_regex(log_message)
    if regex_predicted_class:
        return regex_predicted_class + ' -->regex'
    
    if source != "LegacyCRM":
        sbert_predicted_class = classify_with_sbert(log_message)
        if sbert_predicted_class:
            return sbert_predicted_class + ' -->sbert'
    
    predicted_class = classify_with_llm(log_message)
    return predicted_class + ' -->llm'