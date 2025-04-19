FROM ubuntu:20.04

# Avoids tzdata prompts
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y python3 python3-pip

RUN pip3 install flask

COPY app.py /opt/
WORKDIR /opt

EXPOSE 8080

ENTRYPOINT ["python3", "app.py"]
