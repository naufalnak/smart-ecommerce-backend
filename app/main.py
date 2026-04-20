from fastapi import FastAPI

app = FastAPI(
    title="Smart E-Commerce API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "API is running 🚀"}