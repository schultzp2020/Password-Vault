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

    def insertIntoPassword(self, website, username, password, user):
        # encrypt the data and store it in the database with the user id.
        sql = "INSERT INTO Passwords (personal_identifier, website, username, site_pass) VALUES (%s, %s, %s, %s, %s)"
        val = (user, website, username, password)
        self.cursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, " record inserted.")
        pass

    def removeFromPassword(self, password_id, user):
        # removes a record from the password table
        self.cursor.execute("SELECT * FROM Passwords WHERE id = '" + password_id + "'")
        result = self.cursor.fetchone()
        print(result)
        # self.cursor.execute("DELETE FROM Passwords WHERE id = '" + password_id + "'")
        pass

    def validateLogin(self, username, password):
        # check to see if there is a valid database entry for the username/password combination
        # return the user id on success.
        self.cursor.execute("SELECT * FROM Users WHERE username = '' AND password = ''")
        user = self.cursor.fetchone()
        print(user)
        pass
    
    def addUser(self, username, password):
        # Insert a new row into the users table.
        sql = "INSERT INTO Users (username, user_pass) VALUES (%s, %s)"
        enc_password = 'This is encrypted'
        val = (username, enc_password)
        self.cursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, " record inserted.")
        pass
