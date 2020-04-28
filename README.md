### Flaskapp
Flask documentation can be found [here](https://exploreflask.com/en/latest/index.html)

We're using one file per route

Double-check to make sure the project packages are as listed in 
requirements.txt, a bad version of Flask caused me major problems

NOTE: When testing swagger UI on a deployment server, localhost addresses will not work, they are for local testing only.  
Also, Https will only work if the server is started with https enabled.

Deployment server swagger address: [cs47832.fulgentcorp.com:12137/swagger/](cs47832.fulgentcorp.com:12137/swagger/)

#### To run:
Navigate to the `flaskapp` folder  
To run with http, use `python3 flaskapp.py`  
To run with https, use `python3 flaskapp.py --cert=adhoc`

NOTE: After several *hours* looking, and several more testing, I was unable to find a way to get Flask to handle 
HTTP and HTTPS requests side by side. Even the half-dozen "force https" flask tools refused to work, and at least
one was no longer supported. This appears to be a Flask problem, so please don't grade too harshly. If other people
have gotten it working, please let me know so I can try to implement this.