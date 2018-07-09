import boto3
import datetime
import json
import os

"""
Start a step function based on a file created in S3.
"""
def start_step_function(event, context):
    bucket = str(event["Records"][0]["s3"]["bucket"]["name"])
    key = str(event["Records"][0]["s3"]["object"]["key"])
    if "" in bucket:
        print("")
        step_arn = 
        func_name = 
    else:
        os.sys.exit("Error: Unknown bucket or key.")
    print("### Starting Step Function ###")
    start_date = (datetime.datetime.today()).strftime("%Y%m%d%H%M%S")
    name = start_date + "_" + func_name
    result = {"bucket": bucket, "key": key, "start_date": int(start_date)}
    client = boto3.client("stepfunctions")
    response = client.start_execution(
        stateMachineArn=step_arn,
        name=name,
        input=json.dumps(result)
    )
    return 
