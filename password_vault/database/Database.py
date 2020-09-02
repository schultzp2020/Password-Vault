import mysql.connector
import os

class Database:
    def __init__(self):
        # Create a connection to the database.
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv('database_host'),
                user=os.getenv('database_user'),
                password=os.getenv('database_pass'),
                database=os.getenv('database_schema')
            )
        except Exception as inst:
            print('\nCONNECTION ERROR:', inst, '\nPlease validate .env and try again.\n')
        else:
            self.cursor = self.conn.cursor()
    
    def execute(self, command):
        if self.cursor == None:
            return False

        self.cursor.execute(command)