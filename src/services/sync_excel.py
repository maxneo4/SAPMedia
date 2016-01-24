import pyexcel as pe
import pyexcel.ext.xlsx
import sqlite3


def skip_rows(records, number_rows):
    for i in range(0, number_rows):
        records.pop(0)


def get_data_records(number_columns, records):
    data_records = []
    for item in records:
        if not item[0]:
            break
        data_records.append(item[:number_columns])
        print item
    return data_records


def get_data_from_excel(book_file_name, sheet_name, initial_row, number_columns):
    book = pe.get_book(file_name=book_file_name)
    sheet = book[sheet_name]
    records = sheet.to_array()
    skip_rows(records, initial_row)
    return get_data_records(number_columns, records)


def import_to_database(database_name, insert_query ,data_records):
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()
    cursor.executemany(insert_query, data_records)
    conn.commit()
    conn.close()

