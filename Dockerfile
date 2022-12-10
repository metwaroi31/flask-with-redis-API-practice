FROM python:3.10.9-alpine3.16
WORKDIR /home/app

COPY requirements.txt .
COPY . .
RUN pip3 install -r requirements.txt
RUN apt-get update \
    && apt-get -y install --no-install-recommends mariadb-client build-essential
CMD [ "python3", "run.py", "--port", "5000"]
