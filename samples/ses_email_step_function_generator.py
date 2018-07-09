import boto3
import re
"""
Accepts:
{
    "bucket": "bots-devopsismagic-com", 
    "key": "pippcfcg70ue6ifvnt82504leubctgdo40mrv081", 
    "start_date": "20180709160839"
}

Returns:
Original Data Object
{
    "bucket": "bots-devopsismagic-com", 
    "key": "pippcfcg70ue6ifvnt82504leubctgdo40mrv081", 
    "start_date": "20180709160839",
    "dynamodb": {
        "data": {
            "table": "SesEmailog",
            "record": {
                "receiveDate": start_date,
                "from": email_from,
                "key": key,
                "bucket": bucket
            }
        }
    }
    "cloudwatch":
        data": {
                "log_group": "SesEmailLog",
                "log_stream": "bots",
                "log_events": [
                {
                    "timestamp": "20180709160839",
                    "message": "message"
                }
            ]
        }
    }
}
"""
def ses_generator(event, context):
    bucket = event["bucket"]
    key = event["key"]
    start_date = event["start_date"]
    
    s3 = boto3.resource("s3")

    email_obj = s3.Object(bucket, key)
    email_text = email_obj.get()["Body"].read().decode("utf-8")
    regex = r"Return\-Path\: \<(\S*)\>"
    email_from = re.findall(regex, email_text)[0]
    event["dynamodb"] = {
        "data": {
            "table": "SesEmailog",
            "record": {
                "receiveDate": start_date,
                "from": email_from,
                "key": key,
                "bucket": bucket
            }
        }
    }
    message = "Received email from %s" % email_from
    event["cloudwatch"] = {
    "data": {
                "log_group": "SesEmailLog",
                "log_stream": "bots",
                "log_events": [
                {
                    "timestamp": start_date,
                    "message": message
                }
            ]
        }
    }
    return event
