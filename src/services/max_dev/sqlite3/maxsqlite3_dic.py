import sqlite3
import sys

def open_connection_with_dict_factory(database):
    connection = sqlite3.connect(database)
    connection.row_factory = dict_factory
    return connection


def get_data_as_dictionary(database, query, params):
    try:
        connection = open_connection_with_dict_factory(database)
        cursor = connection.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        connection.close()
        return data
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
