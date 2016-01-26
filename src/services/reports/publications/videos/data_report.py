from max_dev.sqlite3.maxsqlite3 import get_data
from max_dev.root_path import resolve_path


def get_data_report_publications_per(year):
    return get_data(resolve_path('Metrics.db3') ,"""select month,
     corporate_portal_views, corporate_portal_comments,
     news_center_views, news_center_comments,
     sap_tv_views,
     youtube_views, youtube_comments,
     twitter_impressions, twitter_engagement
     from 'metrics per type and year'
     where type = 'video' and year = '{}'""".format(year), ())
