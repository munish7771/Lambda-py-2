import json
import pyodbc
server = 'tcp:myserver.database.windows.net' 
database = 'mydb' 
username = 'myusername' 
password = 'mypassword' 
# to-do later

def handler(event, context):
    
    return {"statusCode": 200, "body": json.dumps({"message": "I'm an HTTP response"})}
    try:
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        cursor.execute('Select @@version;')
        row = cursor.fetchone()
        return {"statusCode": 200, "body": "db version is :" +str(row)}