from flask import render_template
from reports.top_owner import data_report


def quarters_to_months(quarter):
    switcher = {
        "q1": "'01','02','03'",
        "q2": "'04','05','06'",
        "q3": "'07','08','09'",
        "q4": "'10','11','12'"
    }
    return switcher.get(quarter, "nothing")

def get_type(path):
    switcher = {
        "articles": "'article'",
        "videos": "'video'",
        "all": "'article','video'",
    }
    return switcher.get(path, "nothing")


def generate_report_byquarter(year, quarter, type):
    data = data_report.get_data_report_topowner_per_quarter(year, quarters_to_months(quarter), get_type(type))
    title = 'Top contributor {} {} {}'.format(type ,year, quarter.upper())
    return render_template('top_contributor.htm', title=title, data=data)
