from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path

type_headers = {
    "'article'": """sum(corporate_portal_views),
        sum(forbes_views),
        sum(news_center_views),
        sum(business_trends_views)""",
    "'video'": """sum(corporate_portal_views),
        sum(news_center_views),
        sum(sap_tv_views),
        sum(youtube_views)"""
}

def get_data_report__number_views_per_quarter(year, quarter, type):
    headers = type_headers.get(type, 'Nothing')
    return get_data(resolve_path('Metrics.db3') ,"""
    select {}
    from 'Metrics per type and year'
    where year = '{}' and month in ({})
    and type in ({})
    """.format(headers, year, quarter, type), ())


def get_data_report_number_views_per_year(year, type):
    headers = type_headers.get(type, 'Nothing')
    return get_data(resolve_path('Metrics.db3') ,"""
    select {}
    from 'Metrics per type and year'
    where year = '{}'
    and type in ({})
    """.format(headers, year, type), ())


def get_data_report_number_views_per_month(year, month, type):
    headers = type_headers.get(type, 'Nothing')
    return get_data(resolve_path('Metrics.db3') ,"""
    select {}
    from 'Metrics per type and year'
    where year = '{}' and month = '{}'
    and type in ({})
    """.format(headers, year, month, type), ())
