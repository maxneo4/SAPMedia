
def sum_positions(arr, positions):
    sum_value = 0
    for position in positions:
        sum_value+=arr[position]
    return sum_value


def matrix_total(matrix, axis):
    arr_total = [0]*len(axis)
    for row in matrix:
        for axi in axis:
            arr_total[axi-1] += row[axi]
    return arr_total