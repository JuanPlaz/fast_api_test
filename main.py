from fastapi import FastAPI

app = FastAPI() ##Instancia de FastAPI

@app.get("/") ##Path Operation decorator (Usa metodo get).
def home():    ##Path operation function
    return {"Hello": "World"}   ##Json

@app.get("/ciudades")
def ciudades():
    return {"Colombia":"Bogota"}

@app.get("/items/{num_item}")
async def items(num_item):
    return {"num_item":num_item}