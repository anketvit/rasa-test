# -*- coding: utf-8 -*-
"""interacting_w_databse.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RZzOqsJWUWQoObKqFq1HuD4hKao3WzVC
"""

import sqlite3
import pandas as pd

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM eduresource")

    rows = cur.fetchall()

    for row in rows:
        print(row)
        
"""create_connection("resourcesDB")"""
"""select_all_tasks(create_connection("resourcesDB"))"""

def select_by_slot(conn,slot_name,slot_value):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute(f"""SELECT * FROM eduresource
    		WHERE {slot_name}=''{slot_value}''""")

    rows = cur.fetchall()

    for row in rows:
        print(row)

select_by_slot(create_connection("resourcesDB"),slot_name="Type",slot_value="Book")
