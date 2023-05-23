from fastapi import FastAPI, Query
from typing import Union
from pydantic import BaseModel
from enum import Enum
from typing_extensions import Annotated

class Customer(BaseModel):
    name: str
    description: str | None = None 
    # not relevant here, you can use relevant
    price: int 


class Product(BaseModel):
    name: str
    description: str | None = None 
    # not relevant here, you can use relevant
    price: int 
    tax: int | None = None 


class Gender(str, Enum):
    male = "male"
    female = 'female'

app = FastAPI()

@app.get('/', tags=['general'])
def hello():
    return {'message': 'hello world'}


# request Body 
@app.post('/customer', tags = ['customer'])
def add_customer(customer: Customer | None = None, product: Product | None = None):
    if customer:
        return {"customer_name": customer.name, "customer_description": customer.description, "price": customer.price, "tax": customer.tax} 
    else:
        return {'message': "No Customer details"}




@app.get("/customers/{gender}" , tags = ['customer'])
def get_all_customer_by_gender(gender: Gender, offset: int, limit: Annotated[int | None, Query(ge=0, le=10,)] = None):
    # offset: from where the data fetch: starting customer ID, 
    # limit: no. of customer to fetch after starting customer ID
    if limit is not None:
        return {'message': f"Return all customers from {offset} to {offset + limit}, including {offset} and excluding {offset + limit}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.
    else:
        return {'message': f"Return all customers from {offset}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.



@app.get("/customers", tags = ['customer'])
def get_all_customer(offset: int, limit: int | None = None):
    # offset: from where the data fetch: starting customer ID, 
    # limit: no. of customer to fetch after starting customer ID
    if limit is not None:
        return {'message': f"Return all customers from {offset} to {offset + limit}, including {offset} and excluding {offset + limit}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.
    else:
        return {'message': f"Return all customers from {offset}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.



@app.get("/customers", tags = ['customer'])
def get_all_customer(offset: int, limit: Union[int, None] = None):
    # offset: from where the data fetch: starting customer ID, 
    # limit: no. of customer to fetch after starting customer ID
    if limit is not None:
        return {'message': f"Return all customers from {offset} to {offset + limit}, including {offset} and excluding {offset + limit}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.
    else:
        return {'message': f"Return all customers from {offset}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.

