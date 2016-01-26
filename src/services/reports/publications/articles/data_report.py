from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def get_data_report_publications_per(year):
    return get_data(resolve_path('Metrics.db3') ,"""select month,
     corporate_portal_views, corporate_portal_comments,
     forbes_views, forbes_comments,
     news_center_views, news_center_comments,
     business_trends_views, business_trends_comments,
     twitter_impressions, twitter_engagement
     from 'metrics per type and year'
     where type = 'article' and year = '{}'""".format(year), ())
