import os
from .createdb import connect_to_db

conn = connect_to_db()
conn.set_session(autocommit=True)
cur = conn.cursor()

class Base:
    @staticmethod
    def get(table_name, **kwargs):
        for key, val in kwargs.items():
            sql = f"SELECT * FROM politico.{table_name} WHERE {key}='{val}'"
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def get_all(table_name):
        sql = f'SELECT * FROM {table_name}'
        cur.execute(sql)
        data = cur.fetchall()
        return data

    @staticmethod
    def delete(table_name, **kwargs):
        for key, val in kwargs.items():
            sql = f"DELETE * FROM politico.{table_name} WHERE {key}='{val}'"
            cur.execute(sql)
            item = cur.fetchone()
            return item

    @staticmethod
    def update(table_name, keyw='', valuew='', **kwargs):
        for key, val in kwargs.items():
            sql = f"""
            UPDATE politico.{table_name}
            SET {key}='{val}'
            where {keyw}={valuew}"""
            cur.execute(sql)

    @staticmethod
    def insert(table_name, **kwargs):
        data = {}
        for key, val in kwargs.items():
            data[key] = val

        keys = ','.join([key for key in data])
        values = str(tuple(data[key] for key in data))
        sql = f"""INSERT INTO politico.{table_name} ({keys}) VALUES {values}
        RETURNING national_id"""
        cur.execute(sql)
        return cur.fetchone()[0]