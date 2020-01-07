FROM python:latest
WORKDIR /app
RUN apt update
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
ENTRYPOINT ["/usr/local/bin/python", "app.py"]