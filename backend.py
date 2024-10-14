import requests

APIkey = 'bb8c487ce98c5273bfb29176ee18a6a9'


def get_data(place,forecasted_days,type):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}'
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8*forecasted_days
    filtered_data = filtered_data[:nr_values]
    if type == "Temperature":
        filtered_data = [diction['main']['temp'] for diction in filtered_data]
    if type == 'Sky':
        filtered_data = [diction['weather'][0]['main'] for diction in filtered_data]
    return filtered_data


if __name__ == '__main__':
    print(get_data('Noida',3,'Sky'))

    
