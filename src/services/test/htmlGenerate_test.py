import unittest
from reports.publications.articles import report_per_year
from max_dev import maxarray
from max_dev import root_path


class HtmlGenerator(unittest.TestCase):

    root_path.root_path = '../'

    def test_generation_report(self):
        data = report_per_year.get_transformed_data(2015)
        print data

    def test_sum_columns(self):
        data = [['Jan',4,4,4],['Feb',2,-2,4]]
        result = maxarray.sum_total_columns(data, axis_columns=range(1,4))
        self.assertEquals([6, 2, 8], result)
        print result

    def test_sum_total_columns_from_rows(self):
        data = [['Jan',4,4,4],['Feb',2,-2,4], ['March', 10,5,10,5], ['April', 4,4,4]]
        result = maxarray.sum_total_columns_from_rows(data, axis_columns=range(1,4), axis_rows=[0,3])
        self.assertEquals([8, 8, 8], result)
        print result


if __name__ == '__main__':
    unittest.main()
