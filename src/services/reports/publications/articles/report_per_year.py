from flask import render_template
from reports.publications.articles import data_report, processor_data
from reports.report_template_filler import fill_total_year, fill_months


def generate_months_part(transformed_data):
    return fill_months(transformed_data)


def generate_total_year_part(transformed_data):
    return fill_total_year(transformed_data)


def generate_report():
    transformed_data = get_transformed_data()
    rows_and_total = generate_months_part(transformed_data) + generate_total_year_part(transformed_data)
    print rows_and_total
    return render_template('articles_per_year.htm', rows_and_total=rows_and_total)


def get_transformed_data():
    matrix = data_report.get_data_report_publications_per_year()
    return processor_data.process_data(matrix)
