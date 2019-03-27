# microservice
Simple example of a microservice with Flask

Create data folder for mysql image outside microservice project
$ mkdir [...]/data/microservice/mysql

Create the Docker image using Dockerfile
$ docker build -t ccc-microservice/mysql:1.0 .

We should see it with 
$ docker images

Now we can run Docker image with port 3330 (same port will we use for python app) 
$ docker run --name mydatabase -v [...]/data/microservice/mysql:/var/lib/mysql -p 3306:3306 -d ccc-microservice/mysql:1.0

We can verify with
$ docker ps

now, test an INSERT sql command
$ docker exec -i mydatabase mysql -h localhost --port=5000 -u mysql -p -D microservice -e "INSERT INTO buttonpushed(button_date) VALUES (NOW());"

and a SELECT sql command
$ docker exec -i mydatabase mysql -h localhost --port=5000 -u mysql -p -D microservice -e "SELECT * FROM buttonpushed;"
