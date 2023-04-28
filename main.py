
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI() ##Instancia de FastAPI

#Models
class Person(BaseModel):    ##Creation of the constructor with Pydantic
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None    #Optional parameters of the Person class 
    is_married: Optional[bool] = None   #It is not define, the variable can be None.


@app.get("/") ##Path Operation decorator (Use get method).
def home():    ##Path operation function
    return {"Hello": "World"}   ##Json

#Request and Response Body 
@app.post("/person/new")
def create_person(person: Person = Body(...)):  #"person" parameter of "Person" class. Request Body is mandatory.
    return person

@app.get("/person/detail") ##Endpoint, it receives query parameters.
def show_person(
    name: Optional[str] = Query(
    None, 
    min_length=1, 
    max_length=50,
    title="Person Name",
    description="This is the person name. It is between 1 and 50 characters"
    ),
    age: Optional[str] = Query(
    ...,
    title="Person Age",
    description="This is the person age. It is required"
    )
):
    return {name: age}

#Validations: Path Parameters
@app.get("/person/detail/{person_id}")  ##Endpoint, it receives path parameters.
def show_person(
    person_id: int = Path(
    ...,
    gt=0,
    title="Person Id",
    description="This is the Person Id. Required. It should be greater than 0"
    )
):
    return {person_id: "It exists!!!"}





"""
#Examples:
@app.get("/ciudades")
def ciudades():
    return {"Colombia":"Bogota"}

@app.get("/items/{num_item}")
async def items(num_item):
    return {"num_item":num_item}
    """