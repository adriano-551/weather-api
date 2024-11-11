#!/bin/bash
docker build -t docker.weather-api .
docker run -d --name weather-api -p 56734:80 docker.weather-api