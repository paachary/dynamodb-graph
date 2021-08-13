import json

with open('data.json') as f:
    data = json.load(f)
    #print(data)

    print(len(data['persons']))

    for count in range(0,len(data['persons'])-1):
        for key,value in data['persons'][count].items():
            print(key, value)
