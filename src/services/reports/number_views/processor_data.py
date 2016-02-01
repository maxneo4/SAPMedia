from max_dev import maxarray, maxpercent
from reports.number_views.transformed_data import TransformedData


def process_data(matrix):
    transformed_data = TransformedData()
    transformed_data.values = matrix[0]
    transformed_data.total = maxarray.sum_all_positions(matrix[0])
    transformed_data.percents = calculate_percents(transformed_data)
    return transformed_data


def calculate_percents(transformed_data):
    percents = [None]*len(transformed_data.values)
    for idx, value in enumerate(transformed_data.values):
        result = value*100 / transformed_data.total
        percents[idx] = maxpercent.get_percent_representation_two_decimals(result)
    return percents