import requests

API_KEY = "53a5a58a8ebf0d25df42326e968d48ab"


def get_data(place, forecast_days=None,kind=None):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)

    data = response.json()

    filtered_data = data["list"]
    filtered_data = filtered_data[:8*forecast_days]

    return filtered_data


if __name__ == "main":
    print(get_data(place="Tokyo", forecast_days=3))
