import calendar
from reports.publications.articles import data_report
from max_dev.root_path import resolve_path
from max_dev import maxarray


def transform_matrix(matrix):
    for idx, row in enumerate(matrix):
        matrix[idx] = transform_tuple(row)

def transform_tuple(tuple):
    list_tuple = list(tuple)
    list_tuple[0] = calendar.month_abbr[int(list_tuple[0])]
    list_tuple.append(maxarray.sum_positions(list_tuple, (1,3,5,7)))
    list_tuple.append(maxarray.sum_positions(list_tuple, (2,4,6,8)))
    return list_tuple


def get_rows_from_publications_per_year():
    matrix = data_report.get_data_report_publications_per_year()
    transform_matrix(matrix)
    template = get_template('publications_per_year/month_row.html')
    template_total = get_template('publications_per_year/total_row.html')
    partial_result = ''.join(template.format(*arr) for arr in matrix)
    totales = maxarray.sum_total_columns(matrix, range(1,13))
    return partial_result+template_total.format(*totales)


def get_template(template_name):
    file = open(resolve_path('templates/{}').format(template_name), 'r')
    template = file.read()
    return template