import calendar
import array_operations
from data import data_reports

def get_row_from_publications_per_year(tuple, template):
    list_tuple = list(tuple)
    list_tuple[0] = calendar.month_abbr[int(list_tuple[0])]
    list_tuple.append(array_operations.sum_positions(list_tuple, (1,3,5,7)))
    list_tuple.append(array_operations.sum_positions(list_tuple, (2,4,6,8)))
    return template.format(*list_tuple)

def get_rows_from_publications_per_year():
    matrix = data_reports.get_data_report_publications_per_year()
    template = get_template('row_publication_per_year.html')
    return ''.join( get_row_from_publications_per_year(tuple, template) for tuple in matrix)


def get_template(template_name):
    file = open('templates/{}'.format(template_name), 'r')
    template = file.read()
    return template