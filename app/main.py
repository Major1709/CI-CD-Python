from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/home")
def home():
    return {"message": "Welcome to the home kevi!"}