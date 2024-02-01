# Install Docker

To install docker on your laptop/desktop, download the docker desktop and run the application.

[Docker link to download](https://docs.docker.com/engine/install/) 

# To Run Docker Application

All the code written in class is uploaded as it is. Use the following commands to run:

```
docker-compose up --build
```

This will up the applications but only a single instance/container of the application and one NGINX server instance. To scale the application, use the following command:

```
docker-compose up --build --scale app=3
```

The above command creates three instances of the app. If you want to create more instances of car service, use the following command:

```
docker-compose up --build --scale car=3
```

To run the application in detach mode, use "-d". The following command run in the detach mode:

```
docker-compose up -d --build --scale app=3
```

To see all the containers, use the docker desktop application or use the following command:

```
docker ps
```

To down and remove the containers, use the following command:

```
docker-compose down
```

## References for Learning Docker
[YouTube link for docker learning](https://www.youtube.com/watch?v=3c-iBn73dDE&t=1s)

[My Personal Notes for Docker](https://docs.google.com/document/d/1a0ICx93KavALS6oRRfBqkX4FxIg5kZPok68Bgupvhpk/edit?usp=sharing)
