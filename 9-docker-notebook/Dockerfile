FROM ubuntu:latest

RUN apt-get update \
    && apt-get install -y python3-pip \
    && pip3 install --upgrade pip

RUN pip3 install numpy pandas matplotlib seaborn plotly sklearn

WORKDIR /app

COPY short-lived-full-example.py /app
COPY data/titanic/* /app/data/titanic/

CMD ["python3","-u","./short-lived-full-example.py"]