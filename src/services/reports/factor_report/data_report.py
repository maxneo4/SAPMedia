from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def table_from_factor(factor):
    switcher = {
        "Region": "RegionPublications",
        "Needle": "MoveTheNeedlePublications",
        "BoardArea": "BoardAreaPublications"
    }
    return switcher.get(factor, "nothing")


def column_from_factor(factor):
    switcher = {
        "Region": "region",
        "Needle": "gca",
        "BoardArea": "board_area"
    }
    return switcher.get(factor, "nothing")


def get_data_report_regions(year, months, types, factor):
    return get_data(resolve_path('Metrics.db3') ,"""
    select {0}, sum(total) as total
    from {1}
    where year = '{2}' and month in ({3})  and type in ({4})
    group by {0}
    order by total DESC
    """.format(column_from_factor(factor), table_from_factor(factor), year, months, types), ())