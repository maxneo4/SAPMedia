from flask import render_template
from reports.factor_report import data_report, processor_data
from reports.conversor import quarters_to_months, get_type, get_all_months, get_inmonth
import calendar


def generate_report_byquarter(factor, year, quarter, type):
    data = data_report.get_data_report_regions(year, quarters_to_months(quarter), get_type(type), factor)
    data = processor_data.calculate_percents(data)
    title = '{} {} {} {}'.format(factor, type, year, quarter.upper())
    return render_template('factor_report.htm', title=title, data=data, factor=factor)


def generate_report_byyear(factor, year, type):
    data = data_report.get_data_report_regions(year, get_all_months(), get_type(type), factor)
    data = processor_data.calculate_percents(data)
    title = '{} {} {}'.format(factor, type ,year)
    return render_template('factor_report.htm', title=title, data=data, factor=factor)


def generate_report_bymonth(factor, year, month, type):
    data = data_report.get_data_report_regions(year,  get_inmonth(month), get_type(type), factor)
    data = processor_data.calculate_percents(data)
    title = '{} {} {} {}'.format(factor, type, calendar.month_name[int(month)], year)
    return render_template('factor_report.htm', title=title, data=data, factor=factor)
