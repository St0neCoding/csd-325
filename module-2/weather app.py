import requests

base_url = "https://api.openweathermap.org/data/2.5/weather"
appid = "98ee3a68d1e4fa2de0b10daa70026403"

get_weather = "yes"


def main():
    # city = input("Enter a city: ")
    zipcode = input("Enter the zipcode: ")

    try:
        url = f'{base_url}?zip={zipcode}&units=imperial&APPID={appid}'

        response = requests.get(url)
        unformatted_data = response.json()

        city_name = unformatted_data["name"]
        print(city_name)
        temp = unformatted_data["main"]["temp"]
        print(f'The current temp is: {temp}')

        temp_max = unformatted_data['main']['temp_max']
        print(f'The max temp is: {temp_max}')

        report()

    except KeyError:
        print("invalid zip code")
        main()


def report():
    get_weather = input("Would you like to check another city?: ")
    match get_weather.lower():
        case "yes":
            main()
        case "no":
            print("thank you")
        case _:
            print('please enter "yes" or "no"')
            report()


main()