import json


def test_get_weather_success(client, mocker):
    with open('/tests/london_weather.json') as file:
        london_weather_response = json.load(file)

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = london_weather_response

    mocker.patch('requests.post', return_value=mock_response)

    response = client.get('api/weather/London/UK')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'London'
    assert response.json[0]['sys']['country'] == 'GB'


def test_get_weather_failure(client, mocker):
    with open('/tests/london_weather.json') as file:
        london_weather_response = json.load(file)

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = london_weather_response

    mocker.patch('requests.post', return_value=mock_response)

    response = client.get('api/weather/Londonnnn/UnitedK')

    assert response.status_code == 400


def test_weather_cache(client, mocker):
    with open('/tests/london_weather.json') as file:
        london_weather_response = json.load(file)

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = london_weather_response

    mocker.patch('requests.post', return_value=mock_response)

    response = client.get('api/weather/London/UK')
    response_cache = client.get('api/weather/London/UK')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'London'
    assert response.json[0]['sys']['country'] == 'GB'

    assert response_cache.status_code == 200
    assert len(response_cache.json) == 1
    assert response_cache.json[0]['name'] == 'London'
    assert response_cache.json[0]['sys']['country'] == 'GB'
