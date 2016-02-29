from max_dev import maxexcel
from max_dev.sqlite3 import maxsqlite3
from max_dev.root_path import resolve_path


def import_articles(book_file_name, year):
    data_records = maxexcel.get_data_from_excel(book_file_name=book_file_name,
                                                  sheet_name='Metrics - Articles',
                                                  initial_row=8,
                                                  number_columns=18)
    maxsqlite3.update_data(database=resolve_path('Metrics.db3'),
                           query="DELETE FROM PUBLICATION WHERE strftime('%Y' , date) = ? AND TYPE = 'article' ",
                           params=(year,))
    maxsqlite3.executemany_in_database(database=resolve_path('Metrics.db3'),
                                  insert_query='INSERT INTO PUBLICATION VALUES("article",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,0,0,0)',
                                  matrix_data=data_records)


def import_videos(book_file_name, year):
    data_records = maxexcel.get_data_from_excel(book_file_name=book_file_name,
                                                  sheet_name='Metrics - Videos',
                                                  initial_row=8,
                                                  number_columns=16)
    maxsqlite3.update_data(database=resolve_path('Metrics.db3'),
                           query="DELETE FROM PUBLICATION WHERE strftime('%Y' , date) = ? AND TYPE = 'video' ",
                           params=(year,))
    maxsqlite3.executemany_in_database(database=resolve_path('Metrics.db3'),
                                  insert_query='''INSERT INTO PUBLICATION (type, title, owner, date, gca, board_area, customer, region,
                                  corporate_portal_views, corporate_portal_comments, news_center_views, news_center_comments,
                                  sap_tv_views, youtube_views, youtube_comments, twitter_impressions, twitter_engagement)
                                  VALUES("video",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',
                                  matrix_data=data_records)
