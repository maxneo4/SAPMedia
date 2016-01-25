import unittest
import sys
from business import reportsbusiness
from max_dev import maxarray
from max_dev import root_path


class HtmlGenerator(unittest.TestCase):

    root_path.root_path = '../'

    def test_generation_report(self):
      print reportsbusiness.get_rows_from_publications_per_year()


    def test_sum_columns(self):
        data = [['Jan',4,4,4],['Feb',2,-2,4]]
        print maxarray.sum_total_columns(data, axis=range(1,4))



if __name__ == '__main__':
    unittest.main()
