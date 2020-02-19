# app_get.py
import boto3
import json
from boto3.dynamodb.conditions import And, Attr

def getItem(table_name, key):
  table = dynamodb.Table(table_name)
  response = table.get_item(Key=key)
  return response["Item"]

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")#Scripts for operations on DynamoDB
  obj = dynamodb.Table("WebAccessLog").scan(
	FilterExpression=(Attr("ipaddr").eq("188.45.108.168") & Attr("status").ne(200)))
  print(obj["Count"]) 
