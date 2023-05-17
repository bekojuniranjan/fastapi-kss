from fastapi import FastAPI 
from typing import Union
from enum import Enum 

class Gender(str, Enum):
    male = "male"
    female = 'female'
app = FastAPI() 


@app.get('/')
def hello():
    return {'message': 'hello world'}



@app.get("/customers/{gender}")
def get_all_customer_by_gender(gender: Gender, offset: int, limit: int | None = None):
    # offset: from where the data fetch: starting customer ID, 
    # limit: no. of customer to fetch after starting customer ID
    if limit is not None:
        return {'message': f"Return all customers from {offset} to {offset + limit}, including {offset} and excluding {offset + limit}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.
    else:
        return {'message': f"Return all customers from {offset}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.



@app.get("/customers")
def get_all_customer(offset: int, limit: int | None = None):
    # offset: from where the data fetch: starting customer ID, 
    # limit: no. of customer to fetch after starting customer ID
    if limit is not None:
        return {'message': f"Return all customers from {offset} to {offset + limit}, including {offset} and excluding {offset + limit}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.
    else:
        return {'message': f"Return all customers from {offset}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.



@app.get("/customers")
def get_all_customer(offset: int, limit: Union[int, None] = None):
    # offset: from where the data fetch: starting customer ID, 
    # limit: no. of customer to fetch after starting customer ID
    if limit is not None:
        return {'message': f"Return all customers from {offset} to {offset + limit}, including {offset} and excluding {offset + limit}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.
    else:
        return {'message': f"Return all customers from {offset}"}   # what if we have 10000 customers, band width problem to receive all the customers.  offset and limit.

