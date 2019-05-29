import json
# import pyodbc
import pymssql
server = 'myproductdb.cvk8s0vsxaah.us-east-1.rds.amazonaws.com' 
database = 'colors' 
username = 'root' 
password = 'password' 
# to-do later

def handler(event, context):
    # return {"body": event['httpRequest']}
    # return {"statusCode": 200, "body": json.dumps({"message": "I'm an HTTP response"})}
    if event['httpRequest'] == "GET":
        try:
            cnxn = pymssql.connect(server=server,database=database,user=username,password=password)
            cursor = cnxn.cursor()
            # cursor.execute('Select @@version;') -- for database version.
            cursor.execute('Select name from color;')
            row = cursor.fetchall()
            return {"statusCode": 200, "body": "Colors are :" +str(row)}
        except Exception as e:
            return {"statusCode": 400, "error": "Exception occured in code"}
        finally:
            cnxn.close()
    
    if event['httpRequest'] == "POST":
        try:
            cnxn = pymssql.connect(server=server,database=database,user=username,password=password)
            cursor = cnxn.cursor()
            _name = event['name']
            cursor.execute("INSERT INTO color(name) values (%s)",''+_name)
            cnxn.commit()
            return {"statusCode": 200, "body": "color added to database"}
        except Exception as e:
            return {"statusCode": 400, "error": "Exception occured in code- couldnt add color"}
        finally:
            cnxn.close()
    
    if event['httpRequest'] == "DELETE":
        try:
            cnxn = pymssql.connect(server=server,database=database,user=username,password=password)
            cursor = cnxn.cursor()
            _id = int(event['id'])
            cursor.execute("DELETE FROM color where id = %d",_id)
            cnxn.commit()
            return {"statusCode": 200, "body": "color deleted from database"}
        except Exception as e:
            return {"statusCode": 400, "error": "Exception occured in code- couldnt delete color"}
        finally:
            cnxn.close()

    if event['httpRequest'] == "PUT":
        try:
            cnxn = pymssql.connect(server=server,database=database,user=username,password=password)
            cursor = cnxn.cursor()
            _id = int(event['id'])
            _name = event['name']
            # cursor.execute("update color set name = %s where id = %d",(''+_name,_id))
            cursor.execute("DELETE FROM color where id = %d",_id)
            cursor.execute("INSERT INTO color(name) values (%s)",''+_name)
            cnxn.commit()
            return {"statusCode": 200, "body": "color edited from database"}
        except Exception as e:
            return {"statusCode": 400, "error": "Exception occured in code- couldnt edit color"}
        finally:
            cnxn.close()
    

# def post_handler(event, context):
#     return{"event":event}
