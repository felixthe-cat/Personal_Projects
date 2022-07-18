# https://data.weather.gov.hk/weatherAPI/opendata/opendata.php

import requests

r = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/opendata.php?dataType=HHOT&station=CCH&year=2022&rformat=csv')

print(r.content)