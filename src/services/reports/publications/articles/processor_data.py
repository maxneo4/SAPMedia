import calendar
from max_dev import maxarray
from reports.publications.transformed_data import TransformedData


def process_data(matrix):
    transformed_data = TransformedData()
    transform_matrix(matrix)
    transformed_data.matrix_months=matrix
    transformed_data.total_year=maxarray.sum_total_columns(matrix, range(1,13))
    return transformed_data


def transform_matrix(matrix):
    for idx, row in enumerate(matrix):
        matrix[idx] = transform_tuple(row)


def transform_tuple(tuple):
    list_tuple = list(tuple)
    list_tuple[0] = calendar.month_abbr[int(list_tuple[0])]
    list_tuple.append(maxarray.sum_positions(list_tuple, (1,3,5,7)))
    list_tuple.append(maxarray.sum_positions(list_tuple, (2,4,6,8)))
    return list_tuple