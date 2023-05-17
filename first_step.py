from fastapi import FastAPI  # this is import 

app = FastAPI()  # create instance of the Fast API

# path operation decorator
@app.get('/')  # define operation and method  methods: get, post, put, delete, ... path parameter: '/'   
# path operation function
def home():
    # every thing runs here.
    # return of the content
    return {'message': 'hello world'}