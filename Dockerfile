FROM python:3.10

WORKDIR /api

COPY requirements.txt /api

RUN pip install -r requirements.txt

COPY ./app /api/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]



