import sync_excel
from root_path import resolve_path

def import_articles(book_file_name):
    data_records = sync_excel.get_data_from_excel(book_file_name=book_file_name,
                                                  sheet_name='Metrics - Articles',
                                                  initial_row=7,
                                                  number_columns=18)
    sync_excel.import_to_database(database_name=resolve_path('Metrics.db3'),
                                  insert_query='INSERT INTO PUBLICATION VALUES("article",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0,0,0)',
                                  data_records=data_records)

def import_videos(book_file_name):
    data_records = sync_excel.get_data_from_excel(book_file_name=book_file_name,
                                                  sheet_name='Metrics - Videos',
                                                  initial_row=7,
                                                  number_columns=16)
    sync_excel.import_to_database(database_name=resolve_path('Metrics.db3'),
                                  insert_query='''INSERT INTO PUBLICATION (type, title, owner, date, gca, board_area, customer, region,
                                  corporate_portal_views, corporate_portal_comments, news_center_views, news_center_comments,
                                  sap_tv_views, youtube_views, youtube_comments, twitter_impressions, twitter_engagement)
                                  VALUES("video",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                  data_records=data_records)
