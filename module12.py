import requests


# Task 1:
def get_chuck_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    data = response.json()
    print("Chuck Norris says:")
    print(data["value"])

get_chuck_joke()



# Task 2:
def get_weather():
    city = input("Enter municipality/city: ")

    api_key = "API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        print("City not found, try again.")
        return

    weather_description = data["weather"][0]["description"]
    temp_kelvin = data["main"]["temp"]
    temp_celsius = temp_kelvin - 273.15

    print(f"Weather in {city}:")
    print(f"Condition: {weather_description.capitalize()}")
    print(f"Temperature: {temp_celsius:.1f} °C")

get_weather()