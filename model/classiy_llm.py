from groq import Groq
import dotenv
import os

dotenv.load_dotenv("/home/adarsh_r/ML projects/log_classifcation_system/config/.env")
groq_api_key = os.getenv("GROQ_API_KEY")

groq_client = Groq(api_key= groq_api_key)

def classify_with_llm(log_msg: str):

    prompt = f"""
        Classify the log message into one of these categories: 
        (1) Workflow Error, (2) Deprecation Warning. 
    If not, classify into any one of below categries
    If you can't figure out a category, use Unclassified. 
    - HTTP Status
    - Critical Error
    - Security Alert
    - Error
    - System Notification
    - Resource Usage
    - User Action
    - Unclassified

        NO preamble 
        Log message: {log_msg}"
    """

    response = groq_client.chat.completions.create(
        model= "llama-3.1-8b-instant",
        messages=[{"role": "user","content": prompt}]
    )

    return response.choices[0].message.content
