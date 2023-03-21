import requests

base_url = 'https://pokeapi.co/api/v2/'

# Fetch a pokemon's data from the PokeAPI if found, otherwise
# return None.
def get_pokemon(name_or_id):
  result = requests.get(base_url + 'pokemon/' + name_or_id.lower())
  if result.status_code == 200:
    return result.json()
  return None

# Open a file handle with the write flag for a file called
# pokemon.csv in the current directory.
fh = open("pokemon.csv", "w")
fh.write("name,type\n")

# Iterate through the numbers 1 to 150, fetching each pokemon's
# data and saving their name and first type to a CSV.
for i in range(1, 151):
  pokemon = get_pokemon(str(i))
  if pokemon is not None:
    name = pokemon["name"]
    types = pokemon["types"]
    first_type = types[0]["type"]["name"]
    fh.write(pokemon["name"] + "," + first_type + "\n")

fh.close()
print("Done!")
