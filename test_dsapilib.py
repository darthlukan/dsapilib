from dsapilib import DarkSkyAPI
from pprint import pprint

_API_KEY = None
try:
    _API_KEY = open('api_key', 'r').readlines()[0].strip('\n')
except Exception as e:
    print('Unable to open api_key, caught: {0}'.format(e))


def test_api_key():
    assert isinstance(_API_KEY, str)
    assert _API_KEY is not None


def test_instance():
    inst = DarkSkyAPI(_API_KEY)
    assert isinstance(inst, DarkSkyAPI)
    assert inst.key == _API_KEY


def test_instance_no_key():
    try:
        DarkSkyAPI()
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        DarkSkyAPI(None)
    except Exception as e:
        assert isinstance(e, TypeError)

    try:
        DarkSkyAPI('')
    except Exception as e:
        assert isinstance(e, AttributeError)


def test_get_weather():
    lat = 33.876118
    lon = -117.921410
    module = DarkSkyAPI(_API_KEY)
    weather = module.get_weather(lat, lon)
    pprint(weather)
    assert weather is not None
    assert isinstance(weather, dict)
    assert 'daily' in weather
    assert 'hourly' in weather
    assert 'minutely' in weather
    assert 'currently' in weather
    assert 'timezone' in weather
    assert 'longitude' in weather
    assert 'latitude' in weather
