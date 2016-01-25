from max_dev.root_path import resolve_path


def fill_total_year(transformed_data):
    template_total = get_template('publications_per_year/total_row.html')
    return template_total.format(*transformed_data.total_year)

def fill_months(transformed_data):
    template_months = get_template('publications_per_year/month_row.html')
    return ''.join(template_months.format(*arr) for arr in transformed_data.matrix_months)

def get_template(template_name):
    file = open(resolve_path('templates/{}').format(template_name), 'r')
    template = file.read()
    return template
