from flask import render_template
from reports.number_views import data_report, processor_data
from reports.conversor import quarters_to_months, get_type
import calendar

type_column_names = {
    "'article'": ['Corporate Portal', 'Forbes', 'News Center', 'Business Trends / SCN'],
    "'video'": ['Corporate Portal', 'Forbes', 'News Center', 'Business Trends / SCN']
}


def generate_report_byquarter(year, quarter, type):
    data = data_report.get_data_report__number_views_per_quarter(year, quarters_to_months(quarter), get_type(type))
    transformed_data = processor_data.process_data(data)
    transformed_data.title = '{} number of views % {} {}'.format(type, quarter.upper(), year)
    transformed_data.column_names = type_column_names[get_type(type)]
    return render_template('number_of_views.htm', transformed_data=transformed_data)


def generate_report_byyear(year, type):
    data = data_report.get_data_report_number_views_per_year(year, get_type(type))
    transformed_data = processor_data.process_data(data)
    transformed_data.title = '{} number of views % {}'.format(type, year)
    transformed_data.column_names = type_column_names[get_type(type)]
    return render_template('number_of_views.htm', transformed_data=transformed_data)


def generate_report_bymonth(year, month, type):
    data = data_report.get_data_report_number_views_per_month(year, month, get_type(type))
    transformed_data = processor_data.process_data(data)
    transformed_data.title = '{} number of views % {} {}'.format(type, calendar.month_name[int(month)], year)
    transformed_data.column_names = type_column_names[get_type(type)]
    return render_template('number_of_views.htm', transformed_data=transformed_data)
