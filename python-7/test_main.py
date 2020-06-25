from main import get_temperature, get_status_code
from unittest.mock import patch
import pytest

param_values = [
    (-14.235004, -51.92528, 62, 16),
    (-10.235004, 30.92528, 100, 37),
    (20.235004, 12.92528, 32, 0)]


@patch('main.requests.get')
@pytest.mark.parametrize("lat,lng,tempf,tempc", param_values)
def test_get_temperature_by_lat_lng(requests_get, lat, lng, tempf, tempc):
    # print("entrou")
    temperatura = {
        "currently": {
            "temperature": tempf
        }
    }

    requests_get.return_value.json.return_value = temperatura
    requests_get.status_code = 200
    response = get_temperature(lat, lng)
    assert response == tempc


@patch('main.requests.get')
@pytest.mark.parametrize("lat,lng,tempf,tempc", param_values)
def test_status_code_on(requests_get, lat, lng, tempf, tempc):

    requests_get.return_value.status_code = 200
    response = get_status_code(lat, lng)
    assert response == 200


@patch('main.requests.get')
@pytest.mark.parametrize("lat,lng,tempf,tempc", param_values)
def test_status_code_off(requests_get, lat, lng, tempf, tempc):

    requests_get.return_value.status_code >= 400
    response = get_status_code(lat, lng)
    assert response == 200
