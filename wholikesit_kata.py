import requests

url = "https://api.weather.com/current"

# Headers (extra instructions)
headers = {
    "Authorization": "Bearer ABC123",  # Security token
    "Accept": "application/json",  # Tell the API we want JSON format
    "User-Agent": "MyWeatherApp/1.0"  # Identify our app
}

response = requests.get(url, headers=headers)

print(response.json())  # Shows the response
