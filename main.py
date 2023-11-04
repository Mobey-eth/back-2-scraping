import requests
import json
import time

# Define an API endpoint URL
URL = "http://api.weatherapi.com/v1/current.json"

# Specify the location and API key
params = {
    'q': "London",  # Location
    'key': "0ca136552bb64e1392694648230111"  # Your API key
}

# Send a GET request to the API endpoint with the specified parameters in JSON format
response = requests.get(URL, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract and parse the JSON response
    data = response.json()
    time.sleep(2)
  
    # Extract specific information from the JSON response
    location = data['location']
    city = location['name']
    country = location['country']
    
    current = data['current']
    temp_celsius = current['temp_c']
    condition = current['condition']['text']
    windspeed_mph = current['wind_mph']
    
    # Print the extracted information
    print(f"City: {city}")
    print(f"Country: {country}")
    print(f"Temperature (Celsius): {temp_celsius}°C")
    print(f"Condition: {condition}")
    print(f"Windspeed (MPH): {windspeed_mph} mph")
else:
    # Print an error message if the request failed
    print(f"Request failed with status code {response.status_code}")