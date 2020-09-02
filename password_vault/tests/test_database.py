import sys
from dotenv import load_dotenv
import unittest

sys.path.insert(0, 'D:\Project\Password-Vault\password_vault')
from database.Database import *


class TestDatabase(unittest.TestCase):

    def test_conn(self):
        load_dotenv()
        database = Database()
        self.assertNotEqual(database.cursor, None)