# microservice

Simple example of a microservice with Flask

## Build the database

Create data folder for mysql image outside microservice project
```
mkdir [...]/data/microservice/mysql
```

Create the Docker image using Dockerfile
```
docker build -t ccc-microservice/mysql:1.0 .
```

We should see it with 
```
$ docker images
REPOSITORY                                                  TAG                   IMAGE ID            CREATED             SIZE
ccc-microservice/mysql                                      1.0                   2c88ff86a17f        25 hours ago        288MB
```

## Run the database

Now we can run Docker image with binding port 3306 (port that we will use for python app)
```
docker run --name mydatabase -v [...]/data/microservice/mysql:/var/lib/mysql -p 3306:3306 -d ccc-microservice/mysql:1.0
```

We can verify that the container is running with
```
$ docker ps
CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS                   PORTS                               NAMES
749a7bed31bc        ccc-microservice/mysql:1.0   "/entrypoint.sh mysq…"   4 seconds ago       Up 3 seconds (healthy)   0.0.0.0:3306->3306/tcp, 33060/tcp   mydatabase
```

## Use the database

To use INSERT sql command:
```
docker exec -i mydatabase mysql -h localhost --port=5000 -u mysql -p -D microservice -e "INSERT INTO buttonpushed(button_date) VALUES (NOW());"
```

To use SELECT sql command:
```
docker exec -i mydatabase mysql -h localhost --port=5000 -u mysql -p -D microservice -e "SELECT * FROM buttonpushed;"
```
