from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import logging, json, time 

app = FastAPI(title="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")

class User(BaseModel):
    name: str
    age: int
    
    
class JsonLogger(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(record.created)),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line_no": record.lineno
        }
        return json.dumps(log_record)

# Set up logging
log = logging.getLogger("my_logger")
log.setLevel(logging.DEBUG)
z = logging.FileHandler("app.log")
z.setFormatter(JsonLogger())
log.addHandler(z)
h = logging.StreamHandler()
h.setFormatter(JsonLogger())
log.addHandler(h)


@app.get("/first-endpoint")
async def first_endpoint():
    log.info("First endpoint accessed")
    return {"message": "Hello from the first endpoint!"}

@app.post("/user/registration")
async def register_user(user_details: User):
    log.info(f"Attempting to register user: {user_details.name}, Age: {user_details.age}")
    return {"message": f"User registered successfully: {user_details.name}, Age: {user_details.age}"}

if __name__ == "__main__":
    uvicorn.run("aug_1_2026_session_fastapi:app", host="127.0.0.1", port=8000, reload=True)
   #uvicorn.run(app, host="127.0.0.1", port=8000)