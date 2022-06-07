import requests

API_KEY = "765795467c0f244a273da03cf22535ab"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
city = input("Enter a city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
print(request_url)
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An error occurred.")
