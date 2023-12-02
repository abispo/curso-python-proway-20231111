import requests

if __name__ == "__main__":
    result = requests.get("https://goweather.herokuapp.com/weather/São Paulo")

    print(result.json())