from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Fitness Agent Backend is running"}

