import sys
from dotenv import load_dotenv
import unittest

sys.path.insert(0, 'D:\Project\Password-Vault\password_vault')
from database.Database import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.database = Database()

    def test_conn(self):
        self.assertNotEqual(self.database.cursor, None)

    def test_addUser(self):
        pass

    def test_insertIntoPassword(self):
        self.database.insertIntoPassword('test.com', 'quinnzipse', 'test123', 1)