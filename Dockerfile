FROM python:3.10.9-slim-bullseye
WORKDIR /home/app

COPY requirements.txt .
COPY . .

RUN pip3 install -r requirements.txt
RUN apt-get update \
    && apt-get -y install build-essential
CMD [ "python3", "app.py", "--port", "5000"]
