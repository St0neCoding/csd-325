import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=3")
print(response.status_code)

print(response.json())

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())