import json

with open('sample-data.json', 'r') as f:
    data = json.load(f)

if 'imdata' in data:
    for x in data['imdata']:
        print(x['l1PhysIf']['attributes']['dn'])
