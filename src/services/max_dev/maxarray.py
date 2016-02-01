
def sum_positions(array, positions):
    sum_value = 0
    for position in positions:
        sum_value += array[position]
    return sum_value


def sum_all_positions(array):
    sum_value = 0
    for current_value in array:
        sum_value += current_value
    return sum_value


def sum_total_columns(matrix, axis_columns):
    arr_total = [0]*len(axis_columns)
    for row in matrix:
        for axi in axis_columns:
            arr_total[axi-1] += row[axi]
    return arr_total


def sum_total_columns_from_rows(matrix, axis_columns, axis_rows):
    arr_total = [0]*len(axis_columns)
    for idx_row, row in enumerate(matrix):
        for axi_column in axis_columns:
            if idx_row in axis_rows:
                arr_total[axi_column-1] += row[axi_column]
    return arr_total
