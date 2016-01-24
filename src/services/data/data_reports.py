from data_core import data

def get_data_report_publications_per_year():
    return data.get_data("select * from 'metrics per year'", ())
