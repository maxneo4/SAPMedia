from flask import render_template
from reports.publications.articles import data_report, processor_data
from reports.report_template_filler import fill_total_year, fill_months, fill_quarter


def generate_months_part(transformed_data):
    return fill_months(transformed_data)


def generate_total_year_part(transformed_data):
    return fill_total_year(transformed_data)


def generate_quarter1_part(transformed_data):
    return fill_quarter(transformed_data.quarter1_total, quarter_number='1')


def generate_quarter2_part(transformed_data):
    return fill_quarter(transformed_data.quarter2_total, quarter_number='2')


def generate_quarter3_part(transformed_data):
    return fill_quarter(transformed_data.quarter3_total, quarter_number='3')


def generate_quarter4_part(transformed_data):
    return fill_quarter(transformed_data.quarter4_total, quarter_number='4')


def generate_report(year):
    transformed_data = get_transformed_data(year)
    rows_and_total = generate_months_part(transformed_data) + generate_total_year_part(transformed_data)
    quarters = generate_quarter1_part(transformed_data) + generate_quarter2_part(transformed_data) \
        + generate_quarter3_part(transformed_data) + generate_quarter4_part(transformed_data)
    return render_template('articles_per_year.htm', rows_and_total=rows_and_total, quarters=quarters)


def get_transformed_data(year):
    matrix = data_report.get_data_report_publications_per(year=year)
    return processor_data.process_data(matrix)
