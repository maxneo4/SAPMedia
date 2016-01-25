import calendar
from max_dev import maxarray
from reports.publications.transformed_data import TransformedData


def process_data(matrix):
    transformed_data = TransformedData()
    transform_matrix(matrix)
    transformed_data.matrix_months = matrix
    transformed_data.total_year = maxarray.sum_total_columns(matrix, range(1,13))
    transformed_data.quarter1_total = maxarray.sum_total_columns_from_rows(matrix, range(1,13), axis_rows=range(0,3))
    transformed_data.quarter2_total = maxarray.sum_total_columns_from_rows(matrix, range(1,13), axis_rows=range(3,6))
    transformed_data.quarter3_total = maxarray.sum_total_columns_from_rows(matrix, range(1,13), axis_rows=range(6,9))
    transformed_data.quarter4_total = maxarray.sum_total_columns_from_rows(matrix, range(1,13), axis_rows=range(9,12))
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