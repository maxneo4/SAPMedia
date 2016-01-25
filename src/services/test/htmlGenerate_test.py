import unittest
from business import reports
import array_operations

class HtmlGenerator(unittest.TestCase):


    def test_generation_report(self):
      print reports.get_rows_from_publications_per_year()


    def test_sum_columns(self):
        data = [['Jan',4,4,4],['Feb',2,-2,4]]
        print array_operations.matrix_total(data, axis=range(1,4))




if __name__ == '__main__':
    unittest.main()
