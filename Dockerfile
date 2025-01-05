FROM python:3.11.1-alpine

WORKDIR /var/www/app

ADD  requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install --upgrade pip

COPY . .

EXPOSE 8000/tcp