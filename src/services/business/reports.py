import calendar
import array_operations
from data import data_reports

def transform_matrix(matrix):
    for idx, row in enumerate(matrix):
        matrix[idx] = transform_tuple(row)

def transform_tuple(tuple):
    list_tuple = list(tuple)
    list_tuple[0] = calendar.month_abbr[int(list_tuple[0])]
    list_tuple.append(array_operations.sum_positions(list_tuple, (1,3,5,7)))
    list_tuple.append(array_operations.sum_positions(list_tuple, (2,4,6,8)))
    return list_tuple


def get_rows_from_publications_per_year():
    matrix = data_reports.get_data_report_publications_per_year()
    transform_matrix(matrix)
    template = get_template('row_publication_per_year.html')
    template_total = get_template('row_total_publication_per_year.html')
    partial_result = ''.join(template.format(*arr) for arr in matrix)
    totales = array_operations.matrix_total(matrix, range(1,13))
    return partial_result+template_total.format(*totales)


def get_template(template_name):
    file = open('templates/{}'.format(template_name), 'r')
    template = file.read()
    return template