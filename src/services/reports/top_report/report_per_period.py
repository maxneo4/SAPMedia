from flask import render_template
from reports.top_report import data_report
from reports.conversor import quarters_to_months, get_type, get_all_months
import calendar


def generate_reportTopViewed_byquarter(year, quarter, type):
    data = data_report.get_data_report_topViewed(year, quarters_to_months(quarter), get_type(type))
    title = 'Top viewed {} {} {}'.format(type ,year, quarter.upper())
    return render_template('top_report.htm', title=title, data=(data))


def generate_reportTopViewed_byyear(year, type):
    data = data_report.get_data_report_topViewed(year, get_all_months(), get_type(type))
    title = 'Top viewed {} {}'.format(type ,year)
    return render_template('top_report.htm', title=title, data=(data))


def generate_reportTopViewed_bymonth(year, month, type):
    data = data_report.get_data_report_topViewed(year, "'"+month+"'", get_type(type))
    title = 'Top viewed {} {} {}'.format(type ,calendar.month_name[int(month)], year)
    return render_template('top_report.htm', title=title, data=(data))


def generate_reportTopCommented_byquarter(year, quarter, type):
    data = data_report.get_data_report_topCommented(year, quarters_to_months(quarter), get_type(type))
    title = 'Top commented {} {} {}'.format(type ,year, quarter.upper())
    return render_template('top_report.htm', title=title, data=(data))


def generate_reportTopCommented_byyear(year, type):
    data = data_report.get_data_report_topCommented(year, get_all_months(), get_type(type))
    title = 'Top commented {} {}'.format(type ,year)
    return render_template('top_report.htm', title=title, data=(data))


def generate_reportTopCommented_bymonth(year, month, type):
    data = data_report.get_data_report_topCommented(year, "'"+month+"'", get_type(type))
    title = 'Top commented {} {} {}'.format(type ,calendar.month_name[int(month)], year)
    return render_template('top_report.htm', title=title, data=(data))
