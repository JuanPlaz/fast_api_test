
#Python
from typing import Optional
from enum import Enum   ##Class to validate strings Enumerations.

#Pydantic
from pydantic import BaseModel
from pydantic import Field      ##Required to validate models.

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path   

app = FastAPI() ##Instancia de FastAPI

#Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str = Field(..., min_length=1, max_length=50, example="Sydney" )
    state: str = Field(..., min_length=1, max_length=50, example="NSW")
    country: str = Field(..., min_length=1, max_length=50, example="Australia")

class Person(BaseModel):    ##Creation of the constructor with Pydantic
    first_name: str = Field(..., min_length=1, max_length=50, example="Juan")   ##... (mandatory) Use Field to validate models.
    last_name: str = Field(..., min_length=1, max_length=50, example="Plazas")
    age: int = Field(..., gt=0, le=115, example= 30)
    hair_color: Optional[HairColor] = Field(default=None, example="black")    #Optional parameters of the Person class 
    is_married: Optional[bool] = Field(default=None, example=True)  #It is not define, the variable can be None.

    #class Config: ##Helps to define default information.
     #   schema_extra = {
      #      "example": {
       #         "first_name": "Facundo",
        #        "last_name": "Garcia Martoni",
         #       "age": 21,
          #      "hair_color": "blonde",
           #     "is_married": False
            #}

        #}


@app.get("/") ##Path Operation decorator (Use get method).
def home():    ##Path operation function
    return {"Hello": "World"}   ##Json

#Request and Response Body 
@app.post("/person/new")
def create_person(person: Person = Body(...)):  #"person" parameter of "Person" class. Request Body is mandatory.
    return person

#Validations: Query Parameters
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


#Validations: Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
    ...,
    title="Person ID",
    description="This is the Person ID",
    gt=0
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results


"""
#Examples:
@app.get("/ciudades")
def ciudades():
    return {"Colombia":"Bogota"}

@app.get("/items/{num_item}")
async def items(num_item):
    return {"num_item":num_item}
    """