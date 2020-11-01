How to setup:
$ cd ./starwar_python
$ pip3 install -r requirements.txt

How to run:
$ python3 main.py

How to invoke the service:
$ curl -i http://localhost:5000/starwarships

Assumption:
1. Using Python 3 and Python 3 is installed
2. Local machine port 5000 is available
3. Using RESTful API service
4. Hyperdrive rating sort order in ascending order i.e. fastest starship on the top of the result list
5. Starship without Hyperdrive show at the end of result list with hyperdriverating field = "No Hyperdrive"
