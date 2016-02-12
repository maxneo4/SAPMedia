from flask import render_template
from reports.infographic_publications import data_report
from reports.conversor import quarters_to_months
import calendar


def generate_report_byquarter(year, quarter):
    data = data_report.get_data_report_per_quarter(year, quarters_to_months(quarter))
    title = 'Articles with Infographics {} {}'.format(year, quarter.upper())
    return render_template('infographic_publications.htm', title=title, data=(data))


def generate_report_byyear(year):
    data = data_report.get_data_report_per_year(year)
    title = 'Articles with Infographics {}'.format(year)
    return render_template('infographic_publications.htm', title=title, data=(data))


def generate_report_bymonth(year, month):
    data = data_report.get_data_report_per_month(year, month)
    title = 'Articles with Infographics {} {}'.format(calendar.month_name[int(month)], year)
    return render_template('infographic_publications.htm', title=title, data=(data))

