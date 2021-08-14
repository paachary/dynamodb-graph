import json

with open('data.json') as f:
    data = json.load(f)
    # print(data)
    length = len(data['persons'])
    # print(len(data['persons']))

    for count in range(0, length - 1):
        persondata = {}
        if 'reports_to' in data['persons'][count].keys():
            persondata['name'] = data['persons'][count]['node']
            persondata['sk'] = "mgr_" + data['persons'][count]['reports_to']
            print(persondata)

        if 'pet' in data['persons'][count].keys():
            persondata['name'] = data['persons'][count]['node']
            persondata['sk'] = "pet_" + data['persons'][count]['pet']
            print(persondata)

        if 'friend' in data['persons'][count].keys():
            persondata['name'] = data['persons'][count]['node']
            persondata['sk'] = "friend_" + data['persons'][count]['friend']
            print(persondata)

        if 'type' in data['persons'][count].keys():
            persondata['name'] = data['persons'][count]['node']
            persondata['sk'] = data['persons'][count]['type'][0]
            print(persondata)

        if 'type' in data['persons'][count].keys():
            persondata['name'] = data['persons'][count]['node']
            persondata['sk'] = data['persons'][count]['type'][1]
            print(persondata)

