#!/bin/bash

docker build -t flask-tilegen .
docker run -p 5050:5050 flask-tilegen


# чистка от расплода контейнеров после каждой пересборки:
#   docker container ls --all
#   docker container rm AAA BBB CCC ...
#   docker rmi $(docker images --filter dangling=true -q)

