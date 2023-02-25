FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /plant-disease-classification/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /plant-disease-classification/requirements.txt

COPY . /app/app/app

#CMD [ "uvicorn","leaf_mold:app", "--proxy-headers","--host", "0.0.0.0", "--port", "80" ]