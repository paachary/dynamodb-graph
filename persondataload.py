import json

with open('data.json') as f:
    data = json.load(f)
    #print(data)

    for records in data['persons']:
        for key, value in records.items():
            print(key,":",value)