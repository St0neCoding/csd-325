def city_country(city, country, population=None, language=None):
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" - population {population}"
    if language:
        result += f", {language.title()}"
    return result


print(city_country("Santiago", "Chile"))
print(city_country("San Diego", "United States", 230000000))
print(city_country("London", "England", 30000000, "English"))
