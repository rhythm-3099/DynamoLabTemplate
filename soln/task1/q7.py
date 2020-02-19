# app_update.py
import boto3
from boto3.dynamodb.conditions import And, Attr
import json


if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

  keyVal = {
    "title": "Git Pocket Guide",
    "publisher": "O'Reilly Media"
  }

  ##updatedVal = ["pages", "268"]
  ##updateItem("Books", keyVal, updatedVal)
  obj = dynamodb.Table("Books").scan(
	FilterExpression=Attr("pages").gt(300))
  print(obj["Items"])
