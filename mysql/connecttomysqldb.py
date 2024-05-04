from  mysql.connector import connect
from mysql.connector import Error 
def connect():
    try:
        # method will read the env file and return the config object
        
 
        # connect to database
        # reading the database parameters from the config object
        conn = connect(
            host='localhost',
            database='employee',
            user='root',
            password='admin',
            port=3306
        )
 
        return conn
    except(Exception, Error) as error:
        print(error)