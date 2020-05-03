FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:deadsnakes/ppa
RUN apt-get update -y
RUN apt-get install -y python3.7 python3-pip
RUN pip3 install --upgrade pip

COPY flaskapp/requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

# HAS TO BE THE SAME PORT AS THE ONE WE RUN THE FLASK APP ON
EXPOSE 12137

#ENTRYPOINT [ "python3" ]

CMD python3 flaskapp/flaskapp.py --cert=adhoc