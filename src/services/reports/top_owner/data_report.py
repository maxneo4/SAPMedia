from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def get_data_report_topowner_per_quarter(year, quarter, type):
    return get_data(resolve_path('Metrics.db3') ,"""
    select owner, sum(number) as number
    from topowners
    where year = '{}' and month in({})
    and type in({})
    group by owner
    order by number DESC
    limit 10
    """.format(year, quarter, type), ())


def get_data_report_topowner_per_year(year, type):
        return get_data(resolve_path('Metrics.db3') ,"""
    select owner, sum(number) as number
    from topowners
    where year = '{}'
    and type in({})
    group by owner
    order by number DESC
    limit 10
    """.format(year, type), ())


def get_data_report_topowner_per_month(year, month, type):
    return get_data(resolve_path('Metrics.db3') ,"""
    select owner, sum(number) as number
    from topowners
    where year = '{}' and month = '{}'
    and type in({})
    group by owner
    order by number DESC
    limit 10
    """.format(year, month, type), ())
