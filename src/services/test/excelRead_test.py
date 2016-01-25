import unittest

import metrics_importation
from max_dev import root_path


class XSLMReader(unittest.TestCase):

    root_path.root_path = '../'

    def test_importation_from_excel(self):
        metrics_importation.import_articles('Global Master Deck ENG Articles Q4.xlsm')
        metrics_importation.import_videos('Global Master Deck ENG Articles Q4.xlsm')

if __name__ == '__main__':
    unittest.main()
