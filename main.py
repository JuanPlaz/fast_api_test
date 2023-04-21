from fastapi import FastAPI

app = FastAPI() ##Instancia de FastAPI

@app.get("/") ##Path Operation decorator (Usa metodo get).
def home():    ##Path operation function
    return {"Hello": "World"}   ##Json
