import requests

APIkey = 'bb8c487ce98c5273bfb29176ee18a6a9'


def get_data(place,forecasted_days):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}&units=metric'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8*forecasted_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == '__main__':
    print(get_data('Noida',3))

    
