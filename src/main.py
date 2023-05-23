from fastapi import FastAPI, File, UploadFile
from PIL import Image
from io import BytesIO
from src.efficient_net import Classification

app = FastAPI()

@app.on_event('startup')
def startupevent():
    global clf
    clf = Classification()

@app.post('/classify')
async def classify(file: UploadFile = File()):
    img = Image.open(BytesIO(await file.read()))
    return {'class': clf.predict(img)}


