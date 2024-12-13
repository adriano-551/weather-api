import json


def test_get_weather_success(test_client, mocker):
    with open('/tests/london_weather.json') as file:
        london_weather_response = json.load(file)
    with open('/tests/oslo_weather.json') as file:
        oslo_weather_response = json.load(file)

    mock_response = mocker.MagicMock()

    mock_response.json.return_value = london_weather_response
    mocker.patch('requests.get', return_value=mock_response)

    mock_response.json.return_value = oslo_weather_response
    mocker.patch('requests.get', return_value=mock_response)

    response_london = test_client.get('api/weather/London/UK')

    response_london = test_client.get('api/weather/London/UK')

    assert response_london.status_code == 200
    assert len(response_london.json) == 1
    assert response_london.json[0]['name'] == 'London'
    assert response_london.json[0]['sys']['country'] == 'GB'


def test_get_weather_failure(test_client, mocker):
    with open('/tests/london_weather.json') as file:
        london_weather_response = json.load(file)

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = london_weather_response

    mocker.patch('requests.get', return_value=mock_response)

    response = test_client.get('api/weather/Londonnnn/UnitedK')

    assert response.status_code == 400


def test_weather_cache(test_client, mocker):
    with open('/tests/london_weather.json') as file:
        london_weather_response = json.load(file)

    mock_response = mocker.MagicMock()
    mock_response.json.return_value = london_weather_response

    mocker.patch('requests.get', return_value=mock_response)

    response = test_client.get('api/weather/London/UK')
    response_cache = test_client.get('api/weather/London/UK')

    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['name'] == 'London'
    assert response.json[0]['sys']['country'] == 'GB'

    assert response_cache.status_code == 200
    assert len(response_cache.json) == 1
    assert response_cache.json[0]['name'] == 'London'
    assert response_cache.json[0]['sys']['country'] == 'GB'
