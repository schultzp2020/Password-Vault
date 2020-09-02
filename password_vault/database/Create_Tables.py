import Database

class Seeder(Database):
    def create_tables(self):
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Users(user_id int NOT NULL auto_increment, username varchar(60), user_pass varchar(64), primary key (user_id));')
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Passwords(id int NOT NULL auto_increment, personal_identifier int NOT NULL, website varchar(64), username varchar(124), site_pass varchar(124), primary key (id), foreign key (personal_identifier) references Users(user_id) );')