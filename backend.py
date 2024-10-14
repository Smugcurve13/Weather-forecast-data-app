import requests

APIkey = 'bb8c487ce98c5273bfb29176ee18a6a9'


def get_data(place,forecasted_days=None,type=None):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'
    response = requests.get(url)
    data = response.json()
    return data


if __name__ == '__main__':
    print(get_data(place='Noida'))

    
