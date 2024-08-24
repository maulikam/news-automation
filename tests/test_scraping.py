# news-automation/tests/test_scraping.py

import unittest
from src.scraping.fetch_toi_news import fetch_toi_headlines

class TestScraping(unittest.TestCase):

    def test_fetch_bbc_headlines(self):
        headlines = fetch_toi_headlines()
        self.assertTrue(len(headlines) > 0, "No headlines were fetched.")
        self.assertIsInstance(headlines, list, "Headlines should be a list.")
        self.assertIsInstance(headlines[0], str, "Headlines should contain strings.")

if __name__ == "__main__":
    unittest.main()
