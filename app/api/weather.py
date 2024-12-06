from flask import current_app
from app.models import Weather
import requests
from app.api import bp
from app.api.errors import bad_request


@bp.route('/weather/<str:city>/<str:country>', methods=['GET'])
def get_weather(city: str, country: str):
    weather_response = requests.post(
        'https://api.openweathermap.org/data/2.5/weather?q=' + city + ',' + country + '&appid=' + current_app.config['API_KEY'],
    ).json()

    if weather_response['status'] != 200:
        return bad_request("Error in user request", weather_response['status'])

    weather = Weather(
        country_id=weather_response[0]['sys']['id'],
        weather_type=weather_response[0]['weather']['description'],
        temp=weather_response[0]['main']['temp'],
        pressure=weather_response[0]['main']['temp'],
        humidity=weather_response[0]['main']['temp'],
        temp_min=weather_response[0]['main']['temp_min'],
        temp_max=weather_response[0]['main']['temp_max'],
        country=weather_response[0]['sys']['country'],
        name=weather_response[0]['name'],
    )

    return weather
