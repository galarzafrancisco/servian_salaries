from python:3-alpine

WORKDIR /usr/src/app

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENV SITE_URL='https://jobs.lever.co/servian'

CMD ["python", "main.py"]