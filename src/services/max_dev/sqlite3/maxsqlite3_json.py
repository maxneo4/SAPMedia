from maxsqlite3_dic import open_connection_with_dict_factory
import json
import sys
from max_dev import maxrest

def get_json_data(database, query):
    try:
        connection = open_connection_with_dict_factory(database)
        cursor = connection.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        connection.close()
        return json.dumps(data)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise


def insert_json_data(database, insert_query, insert_data):
    try:
        connection = open_connection_with_dict_factory(database)
        cursor = connection.cursor()
        cursor.execute(insert_query, insert_data)
        connection.commit()
        connection.close()
        return maxrest.build_json_response({'success':True}, 200)
    except:
        print "Unexpected error:", sys.exc_info()[0]
        return maxrest.build_json_response({'success':False}, 500)
        raise

