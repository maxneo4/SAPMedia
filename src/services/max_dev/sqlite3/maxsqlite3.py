import sqlite3
import sys


def get_data(database, query, params):
    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        connection.close()
        return data
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def update_data(database, query, params):
    try:
        connection = sqlite3.connect(database)
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        connection.close()
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def executemany_in_database(database, insert_query ,matrix_data):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.executemany(insert_query, matrix_data)
    conn.commit()
    conn.close()
