FROM python:3.12-slim

COPY ./server.py /app/server.py
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app
RUN ls -al
RUN pip3 install -r requirements.txt

CMD ["python3", "server.py"]