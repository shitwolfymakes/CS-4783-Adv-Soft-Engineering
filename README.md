### Flaskapp
Flask documentation can be found [here](https://exploreflask.com/en/latest/index.html)

We're using one file per route

Double-check to make sure the project packages are as listed in 
requirements.txt, a bad version of Flask caused me major problems

#### To run:
Deployment server swagger address: [https://52.188.183.99:12137/swagger/](https://52.188.183.99:12137/swagger/)

We got the curl tests working locally, so `./test/curltest.sh` to run the tests. You may need to chmod first  
Testing also works with Postman and Swagger

HTTP listens on port 12136  
HTTPS listens on port 12137  
mysql listens on port 12138