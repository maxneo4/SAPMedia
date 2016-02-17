from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def get_data_report_top(table, year, months, type):
    return get_data(resolve_path('Metrics.db3') ,"""
    select title, total
    from {}
    where year = '{}' and month in ({})
    and type in ({})
    order by total DESC
    limit 10
    """.format(table, year, months, type), ())


def get_data_report_topViewed(year, months, type):
    return get_data_report_top('TopViewed', year, months, type)


def get_data_report_topCommented(year, months, type):
    return get_data_report_top('TopCommented', year, months, type)