'''
Dependencies
'''
from transformers import pipeline


# Load the Hugging Face sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")


def sentiment_analyzer(text_to_analyse):
    '''
    Function to analyze sentiment of a given text.

    Args:
    - text_to_analyse (str): The text to be analyzed for sentiment.

    Returns:
    - result (list): A list with a dictionary containing the sentiment label and score.
    '''
    result = sentiment_pipeline(text_to_analyse)

    return result
