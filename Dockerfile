FROM python:3.7-slim

RUN mkdir /web-api

COPY ./app /web-api

WORKDIR /web-api/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python3", "web-api.py"]