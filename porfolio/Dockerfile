FROM python:3.9

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt
RUN mkdir /application
RUN chmod -R 777 /application
COPY . /application
WORKDIR /application