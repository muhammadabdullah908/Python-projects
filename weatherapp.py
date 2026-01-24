import requests

# Ask user for city name
userInput = input("Enter a city: ")

# Your OpenWeatherMap API key
apiKey = "23249cc4652f335870efc7dc69f2d7b0"

# Complete API URL with parameters
url = f"https://api.openweathermap.org/data/2.5/weather?q={userInput}&units=metric&appid={apiKey}"

# Send GET request to the API
weatherData = requests.get(url)

# Check if the request was successful
if weatherData.status_code == 200:
    data = weatherData.json()  # Convert JSON response to Python dictionary

    # Extract useful data
    weather = data["weather"][0]["main"]                # Main weather condition (e.g. Clear, Rain)
    description = data["weather"][0]["description"]     # More detailed weather info (e.g. scattered clouds)
    temp = data["main"]["temp"]                         # Current temperature in °C
    feels_like = data["main"]["feels_like"]             # How temperature feels like
    humidity = data["main"]["humidity"]                 # Humidity percentage
    wind_speed = data["wind"]["speed"]                  # Wind speed in m/s

    # Print formatted weather info
    print(f"\nCity: {userInput}")
    print(f"Weather: {weather} ({description})")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

else:
    print("An error has occurred. Please check the city name or API key.")
