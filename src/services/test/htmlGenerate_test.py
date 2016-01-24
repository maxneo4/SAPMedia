import unittest
from business import reports

class HtmlGenerator(unittest.TestCase):


    def test_something(self):
        print reports.get_rows_from_publications_per_year()


if __name__ == '__main__':
    unittest.main()
