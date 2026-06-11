from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Butler's Pizza API is alive!"}

@app.get("/branches")
def get_branches():
    return [
        {"id": 1, "name": "Kenilworth"},
        {"id": 2, "name": "Claremont"},
        {"id": 3, "name": "Wynberg"},
    ]