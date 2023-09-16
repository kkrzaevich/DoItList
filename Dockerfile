FROM python:3.11
RUN mkdir /DoItList
WORKDIR /DoItList
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x DoItList
RUN chmod a+x /DoItList/docker/doit.sh
CMD ["uvicorn", "DoItList.main:app", "--host", "0.0.0.0", "--port", "80"]