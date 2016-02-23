from max_dev import maxpercent, maxarray


def calculate_percents(data):
    calculated_data = [None]*len(data)
    total = maxarray.sum_total_columns(data, (1,))
    for idx, row in enumerate(data):
        result = row[1]*100 / total[0]
        result = maxpercent.get_percent_representation_two_decimals(result)
        new_row = [row[0], result, row[1]]
        calculated_data[idx] = new_row
    return calculated_data


