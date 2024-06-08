import requests
import json,os

apiKey = "98a8c1bd778101047f9e73e09f8026cc"
url = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

cityName = input("Enter city name: ")

completeUrl = f"{baseURL}{cityName}&appid={apiKey}"

response = requests.get(completeUrl)
data = response.json()
print(data)

# Function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

print("City:", data["name"])
print(f"Temperature: {kelvin_to_celsius(data['main']['temp']):.2f} °C")
print(f"Feels Like: {kelvin_to_celsius(data['main']['feels_like']):.2f} °C")
print(f"Minimum Temperature: {kelvin_to_celsius(data['main']['temp_min']):.2f} °C")
print(f"Maximum Temperature: {kelvin_to_celsius(data['main']['temp_max']):.2f} °C")
print(f"Humidity: {data['main']['humidity']} %")
print(f"Pressure: {data['main']['pressure']} hPa")
print(f"Weather Description: {data['weather'][0]['description']}")
print(f"Wind Speed: {data['wind']['speed']} m/s")
print(f"Wind Direction: {data['wind']['deg']} °")
print(f"Visibility: {data['visibility']} meters")
print(f"The temperature feels like: {kelvin_to_celsius(data['main']['feels_like']):.2f} °C")

os.system(f"say 'the temperature of the {cityName} is {kelvin_to_celsius(data["main"]["temp"]):.2f}°C'")

os.system(f"say 'The minimum temperature of the {cityName} is {kelvin_to_celsius(data['main']['temp_min']):.2f}'")



