import json
import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

# Write Code here

def batch_write(table_name, contents):
  table = dynamodb.Table(table_name)
  batch_start = 0
  lcontent = len(contents)
  with table.batch_writer() as batch:
    for item in contents:
		batch.put_item(Item=item)

def batchWrite(table_name, contents):
  table = dynamodb.Table(table_name)

  with table.batch_writer() as batch:
    for item in contents:
      batch.put_item(Item=item)

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

  fd = open("/home/student/Downloads/DynamoDB-Lab/data/logs/web_access_log.json", "r")
  books_obj = json.loads(fd.read())
  
  
  print(len(books_obj))
  obj = batch_write("WebAccessLog", books_obj)
  print(dynamodb.Table("WebAccessLog").scan()["Items"])
