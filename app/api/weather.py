from flask import current_app
from app.models import WeatherResponse
import requests
from app.api import bp
from app.api.errors import bad_request


@bp.route('/weather/<string:city_name>/<string:country_code>', methods=['GET'])
def get_weather(city_name: str, country_code: str):
    weather_response = requests.post(
        'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + ',' + country_code + '&appid=' + current_app.config['API_KEY'],
    ).json()

    if weather_response['status'] != 200:
        return bad_request("Error in user request", weather_response['status'])

    return WeatherResponse(
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
