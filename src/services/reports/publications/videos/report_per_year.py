from flask import render_template
from reports.publications.videos import data_report, processor_data


def generate_report(year):
    transformed_data = get_transformed_data(year)
    transformed_data.title = 'Videos {}'.format(year)
    return render_template('videos_per_year.htm', transformed_data=transformed_data)


def get_transformed_data(year):
    matrix = data_report.get_data_report_publications_per(year=year)
    return processor_data.process_data(matrix)
