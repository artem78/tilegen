#!/bin/bash

docker build -t flask-tilegen .
docker run -p 5050:5050 flask-tilegen


