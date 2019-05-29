# import json
# def handler(event, context):
#     return event
import pymssql
server = 'myproductdb.cvk8s0vsxaah.us-east-1.rds.amazonaws.com' 
database = 'colors' 
username = 'root' 
password = 'password' 

def convert_to_binaryData(filename):
    with open ("/Users/munishsharma/Documents/GitHub/Lambda-py-2/my-serverless-project/textfile.txt",'rb') as file:
        binaryData = file.read()
    return binaryData

def handler(event, context):
    try:
        cnxn = pymssql.connect(server=server,database=database,user=username,password=password)
        cursor = cnxn.cursor()
        cursor.execute()
        return {"statusCode":200,"body":"done adding image to database"}
    except Exception as e:
        return {"statusCode":400,"body":"couldn't add image - some exception occured."}
    finally:
        cnxn.close()



