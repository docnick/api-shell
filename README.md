# api-shell
Shell of a flask API with dockerized nginx load balancer 

# Getting Started
A (hopefully) simple explanation of how to get up and running.

1) **Link your source**: Docker expects the API source code to exist on your host at:
```
/opt/devops/test-api/
```
The easiest thing to do is create a symlink to map your files to that location.

2) **Build the Docker image for the API**: The docker file exists in the top level of the repo, so just navagate there and type:
```
sudo docker build -t test-api .
```

3) **Start the service**: Run `docker-compose up`, this should start 2 containers: the nginx load balancer and the app container. You can test that everything is working correctly by testing the API.
```
curl -XGET http://127.0.0.1:5000/test
```

4) **Scaling**: To scale the number of workers you are using, you can run `docker-compose scale worker=3`, this will spin up a total of 3 docker containers for your api source.
