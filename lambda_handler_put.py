import json


def lambda_handler(event, context):
    print(event)
    return "Hi There, " + event["Name"]
