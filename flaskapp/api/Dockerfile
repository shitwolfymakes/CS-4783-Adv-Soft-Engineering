#found this in a python flask/ docker guide and testing it out
FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

#for json
ENV STATIC_URL /static
ENV STATIC_PATH /cs4783-adv-software-eng-assignments/flaskapp/static

#flaskapp directory
WORKDIR /flaskapp/api

COPY ./requirements.txt ./
#install reqs
RUN pip install -r requirements.txt

COPY . /flaskapp/api
ENTRYPOINT ["python3"]
CMD ["flaskapp.py"]