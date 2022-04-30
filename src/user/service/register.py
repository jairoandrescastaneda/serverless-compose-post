import json
import os
from logging import basicConfig, getLogger, INFO
import requests
import boto3
from aws_xray_sdk.core import patch_all
import auxiliary
patch_all()

logger = getLogger(__name__)
basicConfig(level=INFO, format='PID:%(process)d %(asctime)s %(name)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

dynamodb = boto3.resource("dynamodb")
TABLE_NAME = os.environ["TABLE_NAME"]



def register(event, context):

    try:

        logger.info("User created")
        user = {"name": "Jairo", "age":auxiliary.convert_data(25)}

        return {"statusCode": 200, "body": json.dumps(user)}

    except Exception as error:
        logger.exception(error)
        return {"statusCode":400, "body":json.dumps({"error":"error"})}


