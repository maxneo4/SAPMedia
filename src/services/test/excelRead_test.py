import unittest
import importation


class XSLMReader(unittest.TestCase):
    def test_something(self):
        importation.import_articles()
        importation.import_videos()

if __name__ == '__main__':
    unittest.main()
