import boto3


def put_node(table_name, attributes, dynamodb=None, endpoint_url="http://localhost:8000"):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=endpoint_url)
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item=attributes
    )
