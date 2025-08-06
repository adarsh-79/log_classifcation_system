from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from schema.user_input import UserInput
from model.classify import classify_log

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"response": "log classification system"}

@app.post("/predict") #predict class
async def classify(log_message: UserInput):
    log_msg_dict = log_message.model_dump(include=["log_message", "source"])
    
    try:
        log_label = classify_log(log_msg_dict)
        output = {"log message label": log_label}

        return JSONResponse(status_code= 200, content= output)
    
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))
    