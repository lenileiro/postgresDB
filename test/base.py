import unittest
from db.createdb import init_db, connect_to_db

class BaseTest(unittest.TestCase):

    def setUp(self):
        init_db()

    def tearDown(self):
        conn = connect_to_db()
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS politico.user CASCADE""")
        conn.commit()
        conn.close()