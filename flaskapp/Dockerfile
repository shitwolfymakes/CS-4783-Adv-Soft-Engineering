FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update -y
RUN apt-get install -y python3.7
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["/bin/bash", "run_both.sh"]
