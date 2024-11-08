from python:3.7-slim

ARG name

ENV NAME=$name

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
