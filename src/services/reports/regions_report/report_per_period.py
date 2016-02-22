from flask import render_template
from reports.regions_report import data_report, processor_data
from reports.conversor import quarters_to_months, get_type, get_all_months, get_inmonth
import calendar


def generate_report_byquarter(year, quarter, type):
    data = data_report.get_data_report_regions(year, quarters_to_months(quarter), get_type(type))
    data = processor_data.calculate_percents(data)
    title = 'Regions {} {} {}'.format(type, year, quarter.upper())
    return render_template('regions_report.htm', title=title, data=data)


def generate_report_byyear(year, type):
    data = data_report.get_data_report_regions(year, get_all_months(), get_type(type))
    data = processor_data.calculate_percents(data)
    title = 'Regions {} {}'.format(type ,year)
    return render_template('regions_report.htm', title=title, data=data)


def generate_report_bymonth(year, month, type):
    data = data_report.get_data_report_regions(year,  get_inmonth(month), get_type(type))
    data = processor_data.calculate_percents(data)
    title = 'Regions {} {} {}'.format(type, calendar.month_name[int(month)], year)
    return render_template('regions_report.htm', title=title, data=data)
