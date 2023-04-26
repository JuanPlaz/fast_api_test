
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query

app = FastAPI() ##Instancia de FastAPI

#Models
class Person(BaseModel):    ##Creación de constructor con Pydantic
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None    #Atributos opcionales de la clase Person
    is_married: Optional[bool] = None   #Se definen variables None en caso de no ser definidas


@app.get("/") ##Path Operation decorator (Usa metodo get).
def home():    ##Path operation function
    return {"Hello": "World"}   ##Json

#Request and Response Body 
@app.post("/person/new")
def create_person(person: Person = Body(...)):  #Parámetro person de clase Person. Request Body obligatorio.
    return person

@app.get("/person/details")
def show_person(
    name: Optional[str] = Query(None, min_length=1, max_length=50),
    age: Optional[str] = Query(...)
):
    return {name: age}


"""
@app.get("/ciudades")
def ciudades():
    return {"Colombia":"Bogota"}

@app.get("/items/{num_item}")
async def items(num_item):
    return {"num_item":num_item}
    """