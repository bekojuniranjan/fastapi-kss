FROM python:3.10-slim-buster


WORKDIR /app 

RUN apt-get update && apt-get install -y build-essential libgl1-mesa-glx gcc g++ libglib2.0-0
    
RUN pip3 install --upgrade pip

copy requirements.txt /app/requirements.txt 
RUN pip3 --no-cache-dir install -r requirements.txt 

RUN apt update --fix-missing 

COPY . /app 

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]