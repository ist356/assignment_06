import requests

# Put your CENT Ischool IoT Portal API KEY here.
APIKEY = "APIKEYHERE"

def get_google_place_details(google_place_id: str) -> dict:
    pass # Implement this function
    
def get_azure_sentiment(text: str) -> dict:
    pass # Implement this function

def get_azure_key_phrase_extraction(text: str) -> dict:
    pass # Implement this function

def get_azure_named_entity_recognition(text: str) -> dict:
    pass # Implement this function


def geocode(place:str) -> dict:
    '''
    Given a place name, return the latitude and longitude of the place.
    Written for example_etl.py
    '''
    header = { 'X-API-KEY': APIKEY }
    params = { 'location': place }
    url = "https://cent.ischool-iot.net/api/google/geocode"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary


def get_weather(lat: float, lon: float) -> dict:
    '''
    Given a latitude and longitude, return the current weather at that location.
    written for example_etl.py
    '''
    header = { 'X-API-KEY': APIKEY }
    params = { 'lat': lat, 'lon': lon, 'units': 'imperial' }
    url = "https://cent.ischool-iot.net/api/weather/current"
    response = requests.get(url, headers=header, params=params)
    response.raise_for_status()
    return response.json()  # Return the JSON response as a dictionary