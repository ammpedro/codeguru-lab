import boto3


def syncTables(event, context):
    source_ddb = boto3.client('dynamodb', 'us-east-1')
    destination_ddb = boto3.client('dynamodb', 'us-west-2')
    sync_ddb_table(source_ddb, destination_ddb)


# Scan returns paginated results, so only partial data will be copied
def sync_ddb_table(source_ddb, destination_ddb):
    source_paginator = source_ddb.get_paginator('scan')
    source_response_iterator = source_paginator.paginate(
        TableName="<FMI1>",
    )

    for page in source_response_iterator:

        destination_ddb.put_item(
            TableName="<FMI2>",
            Item=page['Items']
        )