import os
from psycopg2 import connect

def connect_to_db(config=None):
    db_name = os.getenv("DATABASE_URL")
    conn = connect(db_name)
    conn.set_session(autocommit=True)
    return conn

def create_users_table(cur):
    cur.execute(
        """CREATE TABLE IF NOT EXISTS politico.user (
            id SERIAL NOT NULL,
            national_id int NOT NULL PRIMARY KEY,
            firstname VARCHAR (100) NOT NULL,
            lastname VARCHAR (100) NOT NULL,
            othername VARCHAR (100),
            email VARCHAR (100) NOT NULL,
            phone VARCHAR (100) NOT NULL,
            isadmin BOOLEAN NOT NULL,
            password VARCHAR (250) NOT NULL,
            passporturl VARCHAR (100) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")

def init_db(config=None):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("""CREATE SCHEMA IF NOT EXISTS politico;""")
    create_users_table(cur)
    print('Database created successfully')


if __name__ == '__main__':
    init_db()
