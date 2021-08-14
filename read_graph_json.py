import json
import dynamodb_crud_op


def read_json_file(filename):
    with open(filename) as f:
        data = json.load(f)
        length = len(data['persons'])
        for count in range(0, length):
            person_data = data['persons'][count]
            person_data['sk'] = "name_" + data['persons'][count]['node']
            dynamodb_crud_op.put_node(table_name="person_graph_data", attributes=person_data)

            person_data = {}
            if 'reports_to' in data['persons'][count].keys():
                person_data = data['persons'][count]
                person_data['node'] = data['persons'][count]['node']
                person_data['sk'] = "mgr_" + data['persons'][count]['reports_to']
                dynamodb_crud_op.put_node(table_name="person_graph_data", attributes=person_data)

            person_data = {}
            if 'pet' in data['persons'][count].keys():
                person_data = data['persons'][count]
                person_data['node'] = data['persons'][count]['node']
                person_data['sk'] = "pet_" + data['persons'][count]['pet']
                dynamodb_crud_op.put_node(table_name="person_graph_data", attributes=person_data)

            person_data = {}
            if 'friend' in data['persons'][count].keys():
                person_data = data['persons'][count]
                person_data['node'] = data['persons'][count]['node']
                person_data['sk'] = "friend_" + data['persons'][count]['friend']
                dynamodb_crud_op.put_node(table_name="person_graph_data", attributes=person_data)

            person_data = {}
            if 'type' in data['persons'][count].keys():
                person_data['node'] = data['persons'][count]['node']
                person_data['sk'] = data['persons'][count]['type'][0]
                dynamodb_crud_op.put_node(table_name="person_graph_data", attributes=person_data)

            person_data = {}
            try:
                if data['persons'][count]['type'][1].strip() is not None:
                    person_data['node'] = data['persons'][count]['node']
                    person_data['sk'] = data['persons'][count]['type'][1]
                    dynamodb_crud_op.put_node(table_name="person_graph_data", attributes=person_data)
            except IndexError:
                None
