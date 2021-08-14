import boto3
from boto3.dynamodb.conditions import Key


def query_associate_of_mgr(mgr, dynamodb=None, endpoint_url="http://localhost:8000"):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

    table = dynamodb.Table('person_graph_data')
    response = table.query(
        # Add the name of the index you want to use in your query.
        IndexName="gsi_1",
        KeyConditionExpression=Key('sk').eq(mgr),
    )
    return response['Items']


def query_associate_details(name, dynamodb=None, endpoint_url="http://localhost:8000"):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)

    table = dynamodb.Table('person_graph_data')
    response = table.query(
        KeyConditionExpression=Key('node').eq(name)
    )
    return response['Items']


if __name__ == '__main__':
    query_name = "Tim"
    print(f"Person Data of {query_name}")
    persons = query_associate_details(query_name)
    for person in persons:
        if 'name_' + query_name in person['sk']:
            print(f"Tim's Details: {person}")
        if 'mgr_' in person['sk'][0:4]:
            mgr = person['sk'][4:]
            manager = query_associate_details(mgr)
            for row in manager:
                if 'name_'+mgr in row['sk']:
                    print(f" Tim's Manager Details : {row}")

    associates = query_associate_of_mgr("mgr_"+query_name)
    print(f"Associates reporting to Tim: ")
    for associate in associates:
        print(f"{associate}")
