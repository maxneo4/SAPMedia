from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path

def get_data_report_publications_per_year():
    return get_data(resolve_path('Metrics.db3') ,"select * from 'metrics per year'", ())
