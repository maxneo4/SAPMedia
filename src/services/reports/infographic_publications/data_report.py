from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def get_data_report_per_quarter(year, quarter):
    query = """
    select strftime('%d-%m-%Y',date), title
    from InfographicPublications
    where month in ({})
    and year = '{}'
    """.format(quarter, year)
    return get_data(resolve_path('Metrics.db3') ,query, ())


def get_data_report_per_year(year):
    query = """
    select strftime('%d-%m-%Y',date), title
    from InfographicPublications
    where year = '{}'
    """.format(year)
    return get_data(resolve_path('Metrics.db3'), query, ())


def get_data_report_per_month(year, month):
    query = """
    select strftime('%d-%m-%Y',date), title
    from InfographicPublications
    where month ='{}'
    and year = '{}'
    """.format(month, year)
    return get_data(resolve_path('Metrics.db3') ,query, ())
