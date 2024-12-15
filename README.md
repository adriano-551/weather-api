## Overview ##

This is an API built using Flask and Redis to receive requests for weather data for a city and country. The API caches weather data responses from openweathermap and returns the weather data response as JSON.

Based on a project suggestion from the following source: https://roadmap.sh/projects/weather-api-wrapper-service

This project was built using Tiangolo's uwsgi-nginx-flask-docker image as a base, the project can be found here: https://github.com/tiangolo/uwsgi-nginx-flask-docker/tree/master

## Requirements ##

Docker

## Installation ##

After cloning the project use the following command to set up the docker images.

`docker compose up'

When this is done you can use the following command to run pytest from inside the docker container.

'sudo bash run-tests.sh'

## API Overview ##

'GET /api/weather/<string:city_name>/<string:country_code>'

Gets the current day's weather for a specific city and country, returned in JSON format.