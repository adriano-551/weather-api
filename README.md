## Overview ##

This is an API built using Flask and Redis to receive requests for weather data with a city code. The API caches weather data responses from openweathermap and returns the response as JSON.

Source: https://roadmap.sh/projects/weather-api-wrapper-service

## Requirements ##

Docker

## API Overview ##

'GET /api/weather/<string:city_code>'

Gets the current weather data for the requested city_code