from max_dev import maxpercent
import unittest


class CalculatePercent(unittest.TestCase):

    def test_int(self):
        percent = 5*100/20
        percent_as_string = maxpercent.get_percent_representation(percent)
        self.assertEqual('25%', percent_as_string)

    def test_float(self):
        percent = 3.3333333333*100/9
        percent_as_string = maxpercent.get_percent_representation_two_decimals(percent)
        self.assertEqual('37.04%', percent_as_string)


if __name__ == '__main__':
    unittest.main()
