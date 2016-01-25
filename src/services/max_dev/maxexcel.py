import pyexcel
import pyexcel.ext.xlsx


def skip_rows(matrix, number_rows):
    for i in range(0, number_rows):
        matrix.pop(0)


def get_data_records(matrix, number_columns):
    data_records = []
    for row in matrix:
        if not row[0]:
            break
        data_records.append(row[:number_columns])
    return data_records


def get_data_from_excel(book_file_name, sheet_name, initial_row, number_columns):
    book = pyexcel.get_book(file_name=book_file_name)
    sheet = book[sheet_name]
    matrix = sheet.to_array()
    skip_rows(matrix, number_rows=initial_row-1)
    return get_data_records(matrix, number_columns)




