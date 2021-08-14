# dynamodb-graph

This repository demonstrates the design pattern in Dynamodb to store Many-to-Many Relationships using the Adjacency List Design Pattern.

For this, we are using a simple graphical representation of data shown below: ![alt text](https://github.com/paachary/dynamodb-graph/blob/master/RDF-Graph-Representation-Person-Example.jpg "attached jpeg file link")

The dynamodb table consists of the PK (node) and SK (sk). It also has a global secondary index (gsi_1) with "sk" as the PK.

Note that I have used [Dynamodb Local setup](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html) for testing this code.

## Setting up the data

### Configuring AWS
Configure your AWS access key and secret access key along with the desired region.

### Installing boto3 library for python
```python
pip install boto3
```
### Creating the dynamodb table
Execute createtable.sh script.

This script processes the create-table.json in the same directory as that of the script.

The script creates a table and a Global Secondary Index.

```javascript
sh createtable.sh
```

### Verify the table in AWS (assumes that you are running this command in local environment)
```python
aws dynamodb describe-table --table-name person_graph_data --endpoint-url http://localhost:8000
```

### Loading data into the dynamodb table (assumes that you are running this command in local environment)
Execute the python script: 
```python
python main.py
```
This script refers to [data.json](https://github.com/paachary/dynamodb-graph/blob/master/data.json) under the same directory for loading data into the person_graph_data table.


## Querying the data using Table's PK and Global Secondary Index (assumes that you are running this command in local environment)
```python
python query_graph_data.py
```

This script returns details for Tim (associate), his Manager (Alex) using table's PK.

Using the GSI, the query returns details for Tim's two associates (Sam and Mike).


