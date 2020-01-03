FROM python:${PYTHON_VERSION}
RUN apt update
COPY . . 
ENTRYPOINT ["/usr/local/bin/python", "app.py"]
