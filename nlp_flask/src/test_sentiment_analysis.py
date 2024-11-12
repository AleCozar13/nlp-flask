'''
Dependencies
'''
import unittest
from SentimentAnalysis.sentiment_analisys import sentiment_analyzer


class TestSentimentAnalyzer(unittest.TestCase):
    '''
    Test suite for the sentiment_analyzer function.
    '''

    def test_sentiment_analyzer(self):
        '''
        Tests various sentiment inputs for the sentiment_analyzer function.
        '''
        # Test case for positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1[0]['label'], 'POSITIVE')

        # Test case for negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2[0]['label'], 'NEGATIVE')

        # Test case for neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3[0]['label'], 'NEGATIVE')


if __name__ == '__main__':
    unittest.main()
