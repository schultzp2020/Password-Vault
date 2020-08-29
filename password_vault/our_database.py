import mysql.connector
import os

class Database:
    def __init__(self):
        # Create a mysql
        try:
            self.conn = mysql.connector.connect(
                host=os.getenv('database_host'),
                user=os.getenv('database_user'),
                password=os.getenv('database_pass'),
                database=os.getenv('database_schema')
            )
        except:
            print(Exception)

        self.cursor = self.conn.cursor()

    def create_pass_table(self):
        self.cursor.execute("CREATE TABLE passwords (password VARCHAR(255) )")
