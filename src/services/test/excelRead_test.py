import unittest
import metrics_importation


class XSLMReader(unittest.TestCase):
    def test_something(self):
        metrics_importation.import_articles('Global Master Deck ENG Articles Q4.xlsm')
        metrics_importation.import_videos('Global Master Deck ENG Articles Q4.xlsm')

if __name__ == '__main__':
    unittest.main()
