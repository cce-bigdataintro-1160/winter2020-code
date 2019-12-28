FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3

WORKDIR /app

COPY long-lived-random-generator.py /app

CMD ["python3","-u","./long-lived-random-generator.py"]