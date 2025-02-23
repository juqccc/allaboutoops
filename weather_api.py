import requests

api_key = "897cb7af93dc77cc8639d0935e34a4d6"  # Replace with your actual API key
url = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
        """Fetch weather data using requests, returning only useful information."""
        params = {"q": city, "appid": api_key, "units": "imperial"}

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return "Error :" + "City not found or API error"

        data = response.json()

        return f"City: {data['name']}\nTemperature: {data['main']['temp']}°C\nDescription: {data['weather'][0]['description']}"

#
# # Example usage
# #city = input("Enter a city: ").strip()
# print(fetch_weather(city))
#
#
