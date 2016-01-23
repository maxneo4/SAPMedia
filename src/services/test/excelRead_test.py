import unittest
import sync_excel
import sqlite3


class XSLMReader(unittest.TestCase):
    def test_something(self):
        data_records = sync_excel.get_data_from_excel(book_file_name='Global Master Deck ENG Articles Q4.xlsm',
                                                      sheet_name='Metrics - Articles',
                                                      initial_row=8,
                                                      number_columns=18)
        conn = sqlite3.connect('Metrics.db3')
        cursor = conn.cursor()
        cursor.executemany('INSERT INTO PUBLICATION VALUES("article",?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', data_records)
        conn.commit()
        conn.close()

if __name__ == '__main__':
    unittest.main()
