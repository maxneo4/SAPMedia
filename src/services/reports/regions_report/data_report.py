from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def get_data_report_regions(year, months, types):
    return get_data(resolve_path('Metrics.db3') ,"""
    select region, sum(total) as total
    from RegionPublications
    where year = '{}' and month in ({})  and type in ({})
    group by region
    order by total DESC
    """.format(year, months, types), ())