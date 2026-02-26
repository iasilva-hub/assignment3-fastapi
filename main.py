from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Assignment #3 - FastAPI on Render"}

@app.get("/health")
def health():
    return {"status": "healthy"}
