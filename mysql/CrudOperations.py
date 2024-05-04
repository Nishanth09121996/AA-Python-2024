import mysql.connector
from mysql.connector import Error
class Student:
    def __init__(self,id:int,name:str,class_name:str,age:int,dob:str,country:str):
        self.id = id
        self.name= name
        self.class_name = class_name
        self.age= age
        self.dob = dob
        self.country = country
        self.connection = self.get_connection() 

    def get_connection(self):
        try:
            # method will read the env file and return the config object
            
    
            # connect to database
            # reading the database parameters from the config object
            conn = mysql.connector.connect(
                host='localhost',
                database='student',
                user='root',
                password='admin',
                port=3306
            )    
            self.connection = conn
        except(Exception, Error) as error:
            print(error)
    def create_employee_table(self,query):
        create_table_cursor = self.connection.cursor()
        try:
            create_table_cursor.execute(query)
        except(Exception,Error) as error:
            print(error)
        finally:
            create_table_cursor.close()
    
    def insert_data(self,)