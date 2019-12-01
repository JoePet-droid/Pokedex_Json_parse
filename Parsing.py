import json

with open('pokedex.json') as pokemon:
    data = json.load(pokemon)

for d in data:
    if d['id'] == 150:
        break

for name in data:
    del name['name']['french']
    del name['name']['chinese']
    del name['name']['japanese']
    # print(name)
    with open('pokedex_english.json', 'a') as p:
        json.dump(name, p, indent=2)
        if name['id'] == 150:

            break









