FROM python:3.11
RUN mkdir /DoItList
WORKDIR /DoItList
COPY ./back/requirements.txt .
RUN pip install -r requirements.txt
COPY .env .
COPY ./back .
