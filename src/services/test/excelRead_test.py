import unittest
import metrics_importation
import root_path


class XSLMReader(unittest.TestCase):

    root_path.root_path = '../'

    def test_something(self):
        metrics_importation.import_articles('Global Master Deck ENG Articles Q4.xlsm')
        metrics_importation.import_videos('Global Master Deck ENG Articles Q4.xlsm')

if __name__ == '__main__':
    unittest.main()
