from fastapi import FastAPI
from enum import Enum

class Gender(str, Enum):
    male = 'male'
    female = 'female'


app = FastAPI()

@app.get('/') # 127.0.0.1:8000/
def home():
    return {'message': "hello world"}

#path parameter
# @app.get('/customer/{customer_id}')    # 127.0.0.1:8000/customer/1
# def get_customer(customer_id):  # customer_id -> path parameter
#     return {'message': f"get content of customer id: {customer_id}"}

# path parameter with types

# orders matter

@app.get('/customer/1')  # 127.0.0.1:8000/customer/1
def get_first_customer():
    return {"message": "First Customer"}


@app.get('/customer/{customer_id}')    # 127.0.0.1:8000/customer/1
def get_customer(customer_id: int):  # customer_id -> path parameter
    return {'message': customer_id}

# predefined values 
@app.get('/customer_by_gender/{gender}')
def get_by_gender(gender: Gender):
    if gender.value == 'male':
        return {"message": "I am King"}
    elif gender == Gender.female:
        return {'message': "I am Beautiful Queen"}


# @app.get('/customer/male')
# def get_all_male_customer():
#     return {'message': "all male customer"}

# @app.get('/customer/female')
# def get_all_female_customer():
#     return {'message': "all female customer"}
