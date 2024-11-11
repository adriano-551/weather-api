## Overview ##

This is an API built using Flask and Redis to receive requests for weather data with a city code. The API caches weather data responses from openweathermap and returns the response as JSON.

Based on a project suggestion from the following source: https://roadmap.sh/projects/weather-api-wrapper-service

This project was built using Tiangolo's uwsgi-nginx-flask-docker image as a base, the project can be found here: https://github.com/tiangolo/uwsgi-nginx-flask-docker/tree/master

## Requirements ##

Docker

## Installation ##

After cloning the project use the following command to set up the docker image.

`sudo bash run-docker.sh'

When this is done you can use the following command to run pytest from inside the docker container.

'sudo bash run-tests.sh'

## API Overview ##

'GET /api/weather/<string:city_code>'

Gets the current weather data for the requested city_code