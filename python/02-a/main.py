# import json
import requests
import sys

base_url = 'https://pokeapi.co/api/v2/'

def get_pokemon(name):
  response = requests.get(base_url + 'pokemon/' + name.lower())
  if response.status_code != 200:
    return None
  return response.json()

if len(sys.argv) >= 2:
  name = sys.argv[1]
  types = []
  pokemon = get_pokemon(name)
  if pokemon is None:
    print("Pokemon " + name + " does not exist")
  else:
    for t in pokemon['types']:
      types.append(t["type"]["name"])
    typestring = "/".join(types)
    article = 'an' if typestring[0] in 'aeiou' else 'a'
    print(pokemon["name"] + " is " + article + " " + typestring + " pokemon")
else:
  print("Please provide a Pokemon name")
