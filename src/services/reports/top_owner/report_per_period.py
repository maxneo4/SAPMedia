from flask import render_template
from reports.top_owner import data_report
from reports.conversor import quarters_to_months, get_type
import calendar


def generate_report_byquarter(year, quarter, type):
    data = data_report.get_data_report_topowner_per_quarter(year, quarters_to_months(quarter), get_type(type))
    title = 'Top contributor {} {} {}'.format(type ,year, quarter.upper())
    return render_template('top_contributor.htm', title=title, data=(data))


def generate_report_byyear(year, type):
    data = data_report.get_data_report_topowner_per_year(year, get_type(type))
    title = 'Top contributor {} {}'.format(type ,year)
    return render_template('top_contributor.htm', title=title, data=(data))


def generate_report_bymonth(year, month, type):
    data = data_report.get_data_report_topowner_per_month(year, month, get_type(type))
    title = 'Top contributor {} {} {}'.format(type ,calendar.month_name[int(month)], year)
    return render_template('top_contributor.htm', title=title, data=(data))
